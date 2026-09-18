"""Loading the decks and turning them into a board for a given day."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

DECKS = {
    "vocab": {
        "title": "Vocab",
        "icon": "📘",
        "noun": "word",
        "reveal": "Definition",
        "column_width": 240,
        "file": "vocab.json",
    },
    "quant": {
        "title": "Quant",
        "icon": "📐",
        "noun": "concept",
        "reveal": "Answer",
        "column_width": 300,
        "file": "quant.json",
    },
}

SHUFFLE_MODES = {
    "none": "Default order",
    "within": "Shuffle within groups",
    "all": "Shuffle all",
}

TOTAL_DAYS = 16


@st.cache_data(show_spinner=False)
def load_deck(deck: str) -> dict[str, Any]:
    path = DATA_DIR / DECKS[deck]["file"]
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing - run `python scripts/build_data.py` to build it from the workbook."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    if len(data["groups"]) != TOTAL_DAYS:
        raise ValueError(f"{path.name} has {len(data['groups'])} groups, expected {TOTAL_DAYS}.")
    return data


def deck_totals(deck: str) -> list[int]:
    return [len(group["items"]) for group in load_deck(deck)["groups"]]


def items_up_to(deck: str, day: int) -> list[dict[str, Any]]:
    """Every item that is in play on `day` (groups 1..day)."""
    out: list[dict[str, Any]] = []
    for group in load_deck(deck)["groups"][:day]:
        out.extend(group["items"])
    return out


@st.cache_data(show_spinner=False)
def build_board(deck: str, day: int, shuffle: str, reshuffle: int = 0) -> dict[str, Any]:
    """Columns + per-item detail for `day`, honouring the shuffle setting."""
    groups = load_deck(deck)["groups"][:day]
    rng = random.Random(f"{deck}|{day}|{shuffle}|{reshuffle}")

    details: dict[str, dict[str, Any]] = {}
    for group in groups:
        for item in group["items"]:
            details[item["id"]] = {
                "title": item["label"],
                "group": group["title"],
                "blocks": item["blocks"],
            }

    if shuffle == "all":
        # Deal the items of the revealed groups (1..day, never any later ones)
        # back across those same columns, keeping each column's size and title.
        pool = [item for group in groups for item in group["items"]]
        rng.shuffle(pool)
        columns, start = [], 0
        for group in groups:
            size = len(group["items"])
            chunk = pool[start : start + size]
            start += size
            columns.append(
                {
                    "title": group["title"],
                    "items": [{"id": i["id"], "label": i["label"]} for i in chunk],
                }
            )
        # An item can now sit in a different column than it belongs to, so the
        # detail panel says where it actually came from.
        for detail in details.values():
            detail["group"] = f"from {detail['group']}"
        return {"columns": columns, "details": details}

    columns = []
    for group in groups:
        items = list(group["items"])
        if shuffle == "within":
            rng.shuffle(items)
        columns.append(
            {
                "title": group["title"],
                "items": [{"id": i["id"], "label": i["label"]} for i in items],
            }
        )
    return {"columns": columns, "details": details}


def tally(deck: str, day: int, marks: dict[str, str]) -> dict[str, int]:
    items = items_up_to(deck, day)
    green = sum(1 for item in items if marks.get(item["id"]) == "green")
    red = sum(1 for item in items if marks.get(item["id"]) == "red")
    return {"total": len(items), "green": green, "red": red, "left": len(items) - green - red}
