"""Build the JSON decks the Streamlit app reads.

    python scripts/build_data.py            # rebuild data/vocab.json + data/quant.json
    python scripts/build_data.py --check    # rebuild and fail if anything looks off

Vocab comes from the "New Words" sheet of data/GRE_Prep.xlsx: one row is one
word, rows keep their sheet order and are split into 16 even groups.

Quant comes from content/quant/*.md, one file per day, written in this shape:

    # Day title

    ## Concept title
    covers: 12, 13

    Explanation paragraphs.

    ### Example
    A worked example.

    ### Watch out
    An optional trap.

`covers:` lists the audit ids from content/quant/_source_concepts.json - the
frozen list of the 162 concepts in the original spreadsheet - so the rewrite can
be checked for completeness. Every id must be claimed by exactly one entry.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "data" / "GRE_Prep.xlsx"
QUANT_CONTENT = ROOT / "content" / "quant"
SOURCE_CONCEPTS = QUANT_CONTENT / "_source_concepts.json"
OUT_DIR = ROOT / "data"

VOCAB_SHEET = "New Words"
GROUP_COUNT = 16


def cell(value) -> str:
    if value is None:
        return ""
    return re.sub(r"[ \t]+", " ", str(value)).strip()


def norm(title: str) -> str:
    return re.sub(r"\s+", " ", title.strip().lower())


def item_id(prefix: str, text: str) -> str:
    return f"{prefix}{hashlib.md5(norm(text).encode('utf-8')).hexdigest()[:10]}"


def chunk_evenly(items: list, n_groups: int) -> list[list]:
    """Split a list into n_groups chunks whose sizes differ by at most one."""
    base, extra = divmod(len(items), n_groups)
    out, start = [], 0
    for i in range(n_groups):
        size = base + (1 if i < extra else 0)
        out.append(items[start : start + size])
        start += size
    return out


# --------------------------------------------------------------------------- vocab


def build_vocab(warnings: list[str]) -> dict:
    workbook = load_workbook(WORKBOOK, data_only=True, read_only=True)
    if VOCAB_SHEET not in workbook.sheetnames:
        raise SystemExit(f"Sheet {VOCAB_SHEET!r} not found in {WORKBOOK.name}")
    rows = []
    for raw in workbook[VOCAB_SHEET].iter_rows(min_row=2, max_col=4, values_only=True):
        row = [cell(v) for v in raw] + [""] * 4
        if any(row[:4]):
            rows.append(row[:4])
    workbook.close()

    items, seen = [], set()
    for word, definition, synonyms, example in rows:
        if not word:
            continue
        if norm(word) in seen:
            warnings.append(f"vocab: duplicate word {word!r} (keeping the first entry)")
            continue
        seen.add(norm(word))
        blocks = [{"label": "Definition", "text": definition}]
        if synonyms:
            blocks.append({"label": "Synonyms", "text": synonyms})
        if example:
            blocks.append({"label": "Example", "text": example})
        items.append({"id": item_id("v", word), "label": word, "blocks": blocks})
        if not definition:
            warnings.append(f"vocab: {word!r} has no definition")

    groups = [
        {"title": f"Vocab {index}", "items": chunk}
        for index, chunk in enumerate(chunk_evenly(items, GROUP_COUNT), start=1)
    ]
    return {"deck": "vocab", "noun": "word", "groups": groups}


# --------------------------------------------------------------------------- quant


def parse_day(path: Path, warnings: list[str]) -> dict:
    """Parse one content/quant/NN-*.md file into a group of entries."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise SystemExit(f"{path.name}: first line must be '# Day title'")

    group = {"title": lines[0][2:].strip(), "items": []}
    entry: dict | None = None
    block: dict | None = None

    def close_block() -> None:
        nonlocal block
        if entry is not None and block is not None:
            text = "\n".join(block["lines"]).strip()
            if text:
                entry["blocks"].append({"label": block["label"], "text": text})
            else:
                warnings.append(f"{path.name}: {entry['label']!r} has an empty {block['label']!r}")
        block = None

    def close_entry() -> None:
        nonlocal entry
        close_block()
        if entry is not None:
            if not entry["covers"] and not entry["new"]:
                warnings.append(f"{path.name}: {entry['label']!r} has no 'covers:' line")
            if not entry["blocks"]:
                warnings.append(f"{path.name}: {entry['label']!r} has no explanation")
            group["items"].append(entry)
        entry = None

    for line in lines[1:]:
        if line.startswith("## "):
            close_entry()
            label = line[3:].strip()
            entry = {
                "id": item_id("q", label),
                "label": label,
                "covers": [],
                "new": False,
                "split": False,
                "blocks": [],
            }
            block = {"label": "Explanation", "lines": []}
        elif line.startswith("### "):
            close_block()
            block = {"label": line[4:].strip(), "lines": []}
        elif entry is not None and not entry["blocks"] and line.lower().startswith("covers:"):
            # "covers: new" marks a concept added by the rewrite rather than one
            # carried over from the original sheet.
            rest = line.split(":", 1)[1]
            entry["covers"] = [int(n) for n in re.findall(r"\d+", rest)]
            entry["new"] = "new" in rest.lower()
            # "(split)" says on purpose that this source concept is taught across
            # more than one entry, so a second claim on it is not a mistake.
            entry["split"] = "split" in rest.lower()
        elif block is not None:
            block["lines"].append(line)
        elif line.strip():
            warnings.append(f"{path.name}: text outside any concept: {line.strip()[:50]!r}")
    close_entry()
    return group


def build_quant(warnings: list[str]) -> dict:
    files = sorted(QUANT_CONTENT.glob("[0-9]*.md"))
    if len(files) != GROUP_COUNT:
        raise SystemExit(
            f"expected {GROUP_COUNT} day files in {QUANT_CONTENT.relative_to(ROOT)}, found {len(files)}"
        )

    groups = [parse_day(path, warnings) for path in files]

    # Every concept from the original sheet must still be covered, exactly once.
    source = json.loads(SOURCE_CONCEPTS.read_text(encoding="utf-8"))["concepts"]
    claimed: dict[int, list[dict]] = {}
    for group in groups:
        for item in group["items"]:
            for audit_id in item["covers"]:
                claimed.setdefault(audit_id, []).append(item)
    for audit_id, items in sorted(claimed.items()):
        if str(audit_id) not in source:
            warnings.append(f"quant: {items[0]['label']!r} covers unknown source concept {audit_id}")
        elif len(items) > 1 and not all(i["split"] for i in items):
            warnings.append(
                f"quant: source concept {audit_id} ({source[str(audit_id)][:40]!r}) is claimed by "
                f"{len(items)} entries without '(split)': {[i['label'] for i in items]}"
            )
    for audit_id, title in sorted(source.items(), key=lambda kv: int(kv[0])):
        if int(audit_id) not in claimed:
            warnings.append(f"quant: source concept {audit_id} ({title[:60]!r}) is not covered")

    seen: set[str] = set()
    for group in groups:
        for item in group["items"]:
            if item["label"] in seen:
                warnings.append(f"quant: duplicate concept title {item['label']!r}")
            seen.add(item["label"])
            del item["covers"]  # audit-only, not needed by the app
            del item["new"]
            del item["split"]
    return {"deck": "quant", "noun": "concept", "groups": groups}


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit non-zero if there are warnings")
    args = parser.parse_args()

    warnings: list[str] = []
    decks = {"vocab": build_vocab(warnings), "quant": build_quant(warnings)}

    for name, deck in decks.items():
        path = OUT_DIR / f"{name}.json"
        path.write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")
        sizes = [len(g["items"]) for g in deck["groups"]]
        words = sum(len(b["text"].split()) for g in deck["groups"] for i in g["items"] for b in i["blocks"])
        print(
            f"{name}: {sum(sizes)} items in {len(sizes)} groups {sizes} "
            f"({words:,} words) -> {path.relative_to(ROOT)}"
        )

    for warning in warnings:
        print(f"  ! {warning}")
    if warnings and args.check:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
