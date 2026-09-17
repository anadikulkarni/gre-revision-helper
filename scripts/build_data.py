"""Turn data/GRE_Prep.xlsx into the JSON decks the Streamlit app reads.

    python scripts/build_data.py            # rebuild data/vocab.json + data/quant.json
    python scripts/build_data.py --check    # rebuild and fail if anything looks off

Vocab  ("New Words" sheet): one row == one word.  Rows are kept in sheet order
and split into 16 evenly sized groups (order does not matter for vocab).

Quant  ("Quant Notes" sheet): a row whose Concept cell is empty is a
*continuation* of the concept above it, so its explanation / example is merged
into that concept as an extra block.  Concepts are then arranged into the 16
hand-curated days in scripts/grouping.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grouping import QUANT_GROUPS, VOCAB_GROUP_COUNT  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "data" / "GRE_Prep.xlsx"
OUT_DIR = ROOT / "data"

VOCAB_SHEET = "New Words"
QUANT_SHEET = "Quant Notes"


def cell(value) -> str:
    if value is None:
        return ""
    return re.sub(r"[ \t]+", " ", str(value)).strip()


def norm(title: str) -> str:
    """Normalised concept title used to match the sheet against grouping.py."""
    return re.sub(r"\s+", " ", title.strip().lower())


def item_id(prefix: str, text: str) -> str:
    return f"{prefix}{hashlib.md5(norm(text).encode('utf-8')).hexdigest()[:10]}"


def chunk_evenly(items: list, n_groups: int) -> list[list]:
    """Split a list into n_groups chunks whose sizes differ by at most one."""
    total = len(items)
    base, extra = divmod(total, n_groups)
    out, start = [], 0
    for i in range(n_groups):
        size = base + (1 if i < extra else 0)
        out.append(items[start : start + size])
        start += size
    return out


def read_rows(path: Path, sheet: str, n_cols: int = 4) -> list[list[str]]:
    workbook = load_workbook(path, data_only=True, read_only=True)
    if sheet not in workbook.sheetnames:
        raise SystemExit(f"Sheet {sheet!r} not found in {path.name} ({workbook.sheetnames})")
    rows = []
    for raw in workbook[sheet].iter_rows(min_row=2, max_col=n_cols, values_only=True):
        row = [cell(v) for v in raw] + [""] * n_cols
        if any(row[:n_cols]):
            rows.append(row[:n_cols])
    workbook.close()
    return rows


# --------------------------------------------------------------------------- vocab


def build_vocab(warnings: list[str]) -> dict:
    rows = read_rows(WORKBOOK, VOCAB_SHEET)

    items, seen = [], {}
    for word, definition, synonyms, example in rows:
        if not word:
            continue
        key = norm(word)
        if key in seen:
            warnings.append(f"vocab: duplicate word {word!r} (keeping the first entry)")
            continue
        blocks = [{"label": "Definition", "text": definition}]
        if synonyms:
            blocks.append({"label": "Synonyms", "text": synonyms})
        if example:
            blocks.append({"label": "Example", "text": example})
        entry = {"id": item_id("v", word), "label": word, "blocks": blocks}
        seen[key] = entry
        items.append(entry)
        if not definition:
            warnings.append(f"vocab: {word!r} has no definition")

    groups = []
    for index, chunk in enumerate(chunk_evenly(items, VOCAB_GROUP_COUNT), start=1):
        groups.append({"title": f"Vocab {index}", "items": chunk})
    return {"deck": "vocab", "noun": "word", "groups": groups}


# --------------------------------------------------------------------------- quant


def read_quant_concepts(warnings: list[str]) -> list[dict]:
    """Merge continuation rows (empty Concept cell) into the concept above."""
    concepts: list[dict] = []
    for concept, explanation, question, answer in read_rows(WORKBOOK, QUANT_SHEET):
        if concept:
            concepts.append({"label": concept, "parts": []})
        elif not concepts:
            warnings.append(f"quant: row with no concept before any concept: {explanation[:60]!r}")
            continue
        concepts[-1]["parts"].append(
            {"explanation": explanation, "question": question, "answer": answer}
        )

    out = []
    for concept in concepts:
        parts = [p for p in concept["parts"] if any(p.values())]
        explanations = [p["explanation"] for p in parts if p["explanation"]]
        blocks = []
        if explanations:
            # Several explanation rows for one concept: keep them as numbered notes.
            if len(explanations) == 1:
                blocks.append({"label": "Explanation", "text": explanations[0]})
            else:
                for i, text in enumerate(explanations, start=1):
                    blocks.append({"label": f"Explanation {i}", "text": text})
        else:
            warnings.append(f"quant: {concept['label'][:60]!r} has no explanation")
        examples = [p for p in parts if p["question"] or p["answer"]]
        for i, part in enumerate(examples, start=1):
            suffix = f" {i}" if len(examples) > 1 else ""
            if part["question"]:
                blocks.append({"label": f"Example question{suffix}", "text": part["question"]})
            if part["answer"]:
                blocks.append({"label": f"Example answer{suffix}", "text": part["answer"]})
        out.append({"id": item_id("q", concept["label"]), "label": concept["label"], "blocks": blocks})
    return out


def build_quant(warnings: list[str]) -> dict:
    concepts = read_quant_concepts(warnings)
    by_title = {norm(c["label"]): c for c in concepts}

    groups, used = [], set()
    for title, wanted in QUANT_GROUPS:
        items = []
        for want in wanted:
            key = norm(want)
            concept = by_title.get(key)
            if concept is None:
                warnings.append(f"quant: grouping lists {want!r} but the sheet has no such concept")
                continue
            if key in used:
                warnings.append(f"quant: {want!r} is listed in more than one group")
                continue
            used.add(key)
            items.append(concept)
        groups.append({"title": title, "items": items})

    leftovers = [c for c in concepts if norm(c["label"]) not in used]
    for concept in leftovers:
        smallest = min(groups, key=lambda g: len(g["items"]))
        smallest["items"].append(concept)
        warnings.append(
            f"quant: {concept['label'][:60]!r} is not in grouping.py; "
            f"appended to group {groups.index(smallest) + 1!r}"
        )
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
        print(f"{name}: {sum(sizes)} items in {len(sizes)} groups {sizes} -> {path.relative_to(ROOT)}")

    for warning in warnings:
        print(f"  ! {warning}")
    if warnings and args.check:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
