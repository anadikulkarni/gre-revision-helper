"""Session-level progress state: mark locally, push to the backend on save.

Marks are stored per *day*: pressing G on day 5 records "I knew this on day 5".
Move the slider to day 6 and every item starts unmarked again, which is what
makes the mountain worth climbing a second time.

Marking does **not** touch the network. Every change is applied to the in-memory
document and queued; the queue is pushed when you press Save, when the autosave
timer expires, or when you move to another day. Writing on every keypress is
what tripped GitHub's secondary rate limit, which blocks bursts of writes to the
same endpoint.
"""

from __future__ import annotations

import copy
import time
from typing import Any, Iterable

import streamlit as st

from . import storage
from .storage import StorageError, Store

DOC = "_gre_doc"
PENDING = "_gre_pending"
ERROR = "_gre_store_error"
PROFILE = "_gre_profile"
REVISION = "_gre_revision"
LOADED_AT = "_gre_loaded_at"
DIRTY_SINCE = "_gre_dirty_since"
SAVED_AT = "_gre_saved_at"

# How stale a *clean* in-memory copy may get before a rerun re-reads the remote
# one. Never happens while there are unsaved changes.
AUTO_REFRESH_SECONDS = 300

# Default minutes before queued changes are pushed without being asked. 0 means
# "only when I press Save".
DEFAULT_AUTOSAVE_MINUTES = 2


# --------------------------------------------------------------------------- store


def profile() -> str:
    return st.session_state.get(PROFILE) or ""


def set_profile(name: str) -> None:
    if name != st.session_state.get(PROFILE):
        st.session_state[PROFILE] = name
        st.session_state.pop(DOC, None)
        st.session_state.pop(LOADED_AT, None)
        st.session_state.pop("_gre_store", None)


def get_store() -> Store:
    store = st.session_state.get("_gre_store")
    if store is None:
        store = storage.build_store(st.secrets, profile())
        st.session_state["_gre_store"] = store
    return store


def store_error() -> str:
    return st.session_state.get(ERROR, "")


def _set_error(message: str) -> None:
    st.session_state[ERROR] = message


def pending_count() -> int:
    return len(st.session_state.get(PENDING, []))


def bump_revision() -> int:
    """Changing this forces the board component to rebuild from server state."""
    st.session_state[REVISION] = st.session_state.get(REVISION, 0) + 1
    return st.session_state[REVISION]


def revision() -> int:
    return st.session_state.get(REVISION, 0)


# --------------------------------------------------------------------------- document


def document(refresh: bool = False) -> dict[str, Any]:
    """The progress document for this profile, re-read when it goes stale."""
    stale = (
        DOC in st.session_state
        and not pending_count()
        and time.time() - st.session_state.get(LOADED_AT, 0) > AUTO_REFRESH_SECONDS
    )
    if not (refresh or stale or DOC not in st.session_state):
        return st.session_state[DOC]

    previous = st.session_state.get(DOC)
    try:
        doc = get_store().load()
        _set_error("")
    except StorageError as exc:
        doc = previous or storage.empty_document()
        _set_error(str(exc))
    doc.setdefault("marks", {})
    doc.setdefault("settings", {})
    st.session_state[DOC] = doc
    st.session_state[LOADED_AT] = time.time()
    # Only rebuild the board when the marks really moved (another device), so a
    # routine refresh never yanks the selection out from under you.
    if previous is not None and previous.get("marks") != doc.get("marks"):
        bump_revision()
    return doc


def _apply(doc: dict[str, Any], change: dict[str, Any]) -> None:
    kind = change["kind"]
    marks = doc.setdefault("marks", {})
    settings = doc.setdefault("settings", {})
    if kind == "mark":
        day = marks.setdefault(change["deck"], {}).setdefault(str(change["day"]), {})
        if change["status"]:
            day[change["item"]] = change["status"]
        else:
            day.pop(change["item"], None)
    elif kind == "setting":
        settings.setdefault(change["deck"], {})[change["key"]] = change["value"]
    elif kind == "clear_day":
        marks.get(change["deck"], {}).pop(str(change["day"]), None)
    elif kind == "clear_deck":
        marks.pop(change["deck"], None)
    elif kind == "clear_all":
        doc["marks"] = {}
    elif kind == "replace":
        doc.clear()
        doc.update(copy.deepcopy(change["document"]))
        doc.setdefault("marks", {})
        doc.setdefault("settings", {})


def record(changes: Iterable[dict[str, Any]]) -> None:
    """Apply changes to the in-memory document and queue them. No network."""
    changes = list(changes)
    if not changes:
        return
    local = document()
    for change in changes:
        _apply(local, change)
    st.session_state[PENDING] = st.session_state.get(PENDING, []) + changes
    st.session_state.setdefault(DIRTY_SINCE, time.time())


def save() -> bool:
    """Push the queued changes onto a freshly fetched remote copy.

    Fetching before writing is what lets the phone and the laptop both mark
    things without one of them overwriting the other's day. Returns True when
    there was nothing to do or the push succeeded.
    """
    queue = st.session_state.get(PENDING, [])
    if not queue:
        return True

    store = get_store()
    try:
        remote = store.load()
        remote.setdefault("marks", {})
        remote.setdefault("settings", {})
        for change in queue:
            _apply(remote, change)
        store.save(storage.stamp(remote))
    except StorageError as exc:
        # Keep the queue; the local document already reflects every change.
        _set_error(f"{exc}  ({len(queue)} change(s) still unsaved)")
        return False

    st.session_state[PENDING] = []
    st.session_state.pop(DIRTY_SINCE, None)
    st.session_state[DOC] = remote
    st.session_state[LOADED_AT] = time.time()
    st.session_state[SAVED_AT] = time.time()
    _set_error("")
    return True


def unsaved_count() -> int:
    return len(st.session_state.get(PENDING, []))


def unsaved_for_seconds() -> float:
    since = st.session_state.get(DIRTY_SINCE)
    return 0.0 if since is None else time.time() - since


def saved_ago() -> float | None:
    saved = st.session_state.get(SAVED_AT)
    return None if saved is None else time.time() - saved


def maybe_autosave(minutes: int) -> bool:
    """Push queued changes once they have been waiting longer than `minutes`."""
    if minutes <= 0 or not unsaved_count():
        return False
    if unsaved_for_seconds() < minutes * 60:
        return False
    return save()


# --------------------------------------------------------------------------- accessors


def marks(deck: str, day: int) -> dict[str, str]:
    return dict(document().get("marks", {}).get(deck, {}).get(str(day), {}))


def all_marks(deck: str) -> dict[str, dict[str, str]]:
    return document().get("marks", {}).get(deck, {})


def setting(deck: str, key: str, default: Any = None) -> Any:
    return document().get("settings", {}).get(deck, {}).get(key, default)


def set_setting(deck: str, key: str, value: Any) -> None:
    if setting(deck, key) == value:
        return
    record([{"kind": "setting", "deck": deck, "key": key, "value": value}])


def streaks_from(marks_by_day: dict[str, dict[str, str]], day: int, item_ids: Iterable[str]) -> dict[str, int]:
    """How many days in a row, ending yesterday, each item has been green.

    Walking backwards from `day - 1` and dropping an item the moment it is not
    green gives the length of its *current* run, which is what the adaptive
    filter uses to retire an item that has been known three days running.
    """
    alive = set(item_ids)
    streaks: dict[str, int] = {}
    for earlier in range(day - 1, 0, -1):
        if not alive:
            break
        day_marks = marks_by_day.get(str(earlier), {})
        for item in list(alive):
            if day_marks.get(item) == "green":
                streaks[item] = streaks.get(item, 0) + 1
            else:
                alive.discard(item)
    return streaks


def green_streaks(deck: str, day: int, item_ids: Iterable[str]) -> dict[str, int]:
    return streaks_from(all_marks(deck), day, item_ids)


def diff_marks(deck: str, day: int, incoming: dict[str, str]) -> list[dict[str, Any]]:
    """Turn a full marks map from the board into the minimal list of changes."""
    current = marks(deck, day)
    changes: list[dict[str, Any]] = []
    for item, status in incoming.items():
        if status in ("green", "red") and current.get(item) != status:
            changes.append({"kind": "mark", "deck": deck, "day": day, "item": item, "status": status})
    for item in current:
        if item not in incoming:
            changes.append({"kind": "mark", "deck": deck, "day": day, "item": item, "status": None})
    return changes


def clear_day(deck: str, day: int) -> None:
    record([{"kind": "clear_day", "deck": deck, "day": day}])
    bump_revision()


def clear_deck(deck: str) -> None:
    record([{"kind": "clear_deck", "deck": deck}])
    bump_revision()


def clear_everything() -> None:
    """Wipe every mark in every deck - used to start a fresh mountain."""
    record([{"kind": "clear_all"}])
    bump_revision()


def replace_document(new_document: dict[str, Any]) -> None:
    record([{"kind": "replace", "document": new_document}])
    bump_revision()
