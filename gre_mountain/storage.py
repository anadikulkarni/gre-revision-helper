"""Where the mountain keeps its progress.

The app writes one small JSON document per profile.  Which backend holds that
document is decided by ``.streamlit/secrets.toml`` (see README):

    local     -- a file next to the app.  Fine on your laptop, but Streamlit
                 Community Cloud wipes the disk on every reboot/redeploy, so it
                 is only a fallback there.
    gist      -- a secret GitHub Gist.  Nothing to set up beyond a token, and it
                 syncs between every device you open the app on.
    supabase  -- a row in a Postgres table, for the same reason.

Every backend implements ``load()`` / ``save()`` over the same document shape::

    {
      "version": 1,
      "updated_at": "2026-09-17T09:00:00+00:00",
      "marks":    {"vocab": {"3": {"v1a2b3c4d5e": "green"}}, "quant": {...}},
      "settings": {"vocab": {"day": 3, "shuffle": "none"}, "quant": {...}}
    }

Writes are applied as small deltas on top of a freshly fetched document (see
progress.apply_changes), so marking words on your phone and then on your laptop
merges instead of one device overwriting the other.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import requests

GIST_DESCRIPTION = "GRE revision mountain progress"
REQUEST_TIMEOUT = 20


class StorageError(RuntimeError):
    """Raised when a backend cannot be reached; the app shows this to the user."""


def empty_document() -> dict[str, Any]:
    return {"version": 1, "updated_at": None, "marks": {}, "settings": {}}


@dataclass
class Store:
    """Base class: a named place to put one JSON document."""

    profile: str = "default"

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def syncs_across_devices(self) -> bool:
        return True

    def load(self) -> dict[str, Any]:
        raise NotImplementedError

    def save(self, document: dict[str, Any]) -> None:
        raise NotImplementedError


# --------------------------------------------------------------------------- local


@dataclass
class LocalFileStore(Store):
    directory: Path = field(default_factory=lambda: Path(".gre_progress"))

    @property
    def name(self) -> str:
        return f"local file ({self.path})"

    @property
    def syncs_across_devices(self) -> bool:
        return False

    @property
    def path(self) -> Path:
        return self.directory / f"progress-{self.profile}.json"

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return empty_document()
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise StorageError(f"Could not read {self.path}: {exc}") from exc

    def save(self, document: dict[str, Any]) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(document, ensure_ascii=False, indent=1), encoding="utf-8")
            tmp.replace(self.path)
        except OSError as exc:
            raise StorageError(f"Could not write {self.path}: {exc}") from exc


# --------------------------------------------------------------------------- gist


@dataclass
class GistStore(Store):
    token: str = ""
    gist_id: str = ""

    @property
    def name(self) -> str:
        return f"GitHub Gist ({self.gist_id or 'auto-discovered'})"

    @property
    def filename(self) -> str:
        return f"gre-mountain-{self.profile}.json"

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def _request(self, method: str, url: str, **kwargs) -> Any:
        try:
            response = requests.request(
                method, url, headers=self._headers(), timeout=REQUEST_TIMEOUT, **kwargs
            )
        except requests.RequestException as exc:
            raise StorageError(f"GitHub is unreachable: {exc}") from exc
        if response.status_code == 401:
            raise StorageError("GitHub rejected the token (needs the 'gist' scope).")
        if not response.ok:
            raise StorageError(f"GitHub returned {response.status_code}: {response.text[:200]}")
        return response.json()

    def _find_gist_id(self) -> str | None:
        page = 1
        while page <= 5:
            gists = self._request("GET", f"https://api.github.com/gists?per_page=100&page={page}")
            if not gists:
                return None
            for gist in gists:
                if self.filename in (gist.get("files") or {}):
                    return gist["id"]
            page += 1
        return None

    def _ensure_gist_id(self, create_with: dict[str, Any] | None = None) -> str:
        if self.gist_id:
            return self.gist_id
        found = self._find_gist_id()
        if found:
            self.gist_id = found
            return found
        if create_with is None:
            return ""
        created = self._request(
            "POST",
            "https://api.github.com/gists",
            json={
                "description": GIST_DESCRIPTION,
                "public": False,
                "files": {self.filename: {"content": json.dumps(create_with, indent=1)}},
            },
        )
        self.gist_id = created["id"]
        return self.gist_id

    def load(self) -> dict[str, Any]:
        gist_id = self._ensure_gist_id()
        if not gist_id:
            return empty_document()
        gist = self._request("GET", f"https://api.github.com/gists/{gist_id}")
        entry = (gist.get("files") or {}).get(self.filename)
        if not entry:
            return empty_document()
        content = entry.get("content") or ""
        if entry.get("truncated") and entry.get("raw_url"):
            try:
                raw = requests.get(entry["raw_url"], timeout=REQUEST_TIMEOUT)
                raw.raise_for_status()
                content = raw.text
            except requests.RequestException as exc:
                raise StorageError(f"Could not fetch the full gist: {exc}") from exc
        if not content.strip():
            return empty_document()
        try:
            return json.loads(content)
        except ValueError as exc:
            raise StorageError(f"The gist does not contain valid JSON: {exc}") from exc

    def save(self, document: dict[str, Any]) -> None:
        gist_id = self._ensure_gist_id(create_with=document)
        if not gist_id:
            raise StorageError("Could not create the progress gist.")
        self._request(
            "PATCH",
            f"https://api.github.com/gists/{gist_id}",
            json={"files": {self.filename: {"content": json.dumps(document, indent=1)}}},
        )


# --------------------------------------------------------------------------- supabase


@dataclass
class SupabaseStore(Store):
    url: str = ""
    key: str = ""
    table: str = "gre_progress"

    @property
    def name(self) -> str:
        return f"Supabase ({self.table})"

    def _headers(self) -> dict[str, str]:
        return {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
        }

    @property
    def _endpoint(self) -> str:
        return f"{self.url.rstrip('/')}/rest/v1/{self.table}"

    def load(self) -> dict[str, Any]:
        try:
            response = requests.get(
                self._endpoint,
                headers=self._headers(),
                params={"id": f"eq.{self.profile}", "select": "document"},
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            raise StorageError(f"Supabase is unreachable: {exc}") from exc
        if not response.ok:
            raise StorageError(f"Supabase returned {response.status_code}: {response.text[:200]}")
        rows = response.json()
        if not rows:
            return empty_document()
        return rows[0].get("document") or empty_document()

    def save(self, document: dict[str, Any]) -> None:
        try:
            response = requests.post(
                self._endpoint,
                headers={**self._headers(), "Prefer": "resolution=merge-duplicates"},
                json=[{"id": self.profile, "document": document}],
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            raise StorageError(f"Supabase is unreachable: {exc}") from exc
        if not response.ok:
            raise StorageError(f"Supabase returned {response.status_code}: {response.text[:200]}")


# --------------------------------------------------------------------------- factory


def _secret(secrets, *path, default=None):
    """Read a nested secret without blowing up when the section is missing."""
    node: Any = secrets
    for key in path:
        try:
            node = node[key]
        except (KeyError, TypeError, AttributeError, FileNotFoundError):
            return default
    return node


def build_store(secrets, profile: str = "") -> Store:
    """Pick a backend from secrets (falling back to a local file)."""
    profile = (
        profile
        or str(_secret(secrets, "storage", "profile", default="") or "")
        or os.environ.get("GRE_PROFILE", "")
        or "default"
    )
    backend = str(_secret(secrets, "storage", "backend", default="") or "").strip().lower()

    gist_token = _secret(secrets, "storage", "gist", "token", default="") or os.environ.get(
        "GRE_GIST_TOKEN", ""
    )
    supabase_url = _secret(secrets, "storage", "supabase", "url", default="") or os.environ.get(
        "GRE_SUPABASE_URL", ""
    )
    supabase_key = _secret(secrets, "storage", "supabase", "key", default="") or os.environ.get(
        "GRE_SUPABASE_KEY", ""
    )

    if not backend:  # auto-detect from whatever credentials are present
        if gist_token:
            backend = "gist"
        elif supabase_url and supabase_key:
            backend = "supabase"
        else:
            backend = "local"

    if backend == "gist":
        if not gist_token:
            raise StorageError("storage.backend is 'gist' but storage.gist.token is missing.")
        return GistStore(
            profile=profile,
            token=str(gist_token),
            gist_id=str(_secret(secrets, "storage", "gist", "gist_id", default="") or ""),
        )
    if backend == "supabase":
        if not (supabase_url and supabase_key):
            raise StorageError(
                "storage.backend is 'supabase' but storage.supabase.url/key are missing."
            )
        return SupabaseStore(
            profile=profile,
            url=str(supabase_url),
            key=str(supabase_key),
            table=str(_secret(secrets, "storage", "supabase", "table", default="gre_progress")),
        )
    if backend != "local":
        raise StorageError(f"Unknown storage backend {backend!r} (use local, gist or supabase).")

    directory = _secret(secrets, "storage", "local", "directory", default="") or os.environ.get(
        "GRE_LOCAL_DIR", ""
    )
    return LocalFileStore(
        profile=profile,
        directory=Path(str(directory)) if directory else Path(".gre_progress"),
    )


def stamp(document: dict[str, Any]) -> dict[str, Any]:
    document["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    return document
