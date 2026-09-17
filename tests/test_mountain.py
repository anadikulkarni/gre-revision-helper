"""Checks for the parts that are easy to get quietly wrong: the deck build,
the day grouping, the shuffle modes and the merge behaviour of the store.

    python -m pytest tests -q
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from gre_mountain import storage  # noqa: E402
from gre_mountain.storage import LocalFileStore, StorageError, build_store  # noqa: E402


def load(name: str) -> dict:
    return json.loads((ROOT / "data" / f"{name}.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- decks


@pytest.mark.parametrize("deck", ["vocab", "quant"])
def test_sixteen_groups(deck):
    assert len(load(deck)["groups"]) == 16


@pytest.mark.parametrize("deck", ["vocab", "quant"])
def test_ids_are_unique_and_items_complete(deck):
    ids, labels = set(), set()
    for group in load(deck)["groups"]:
        assert group["items"], f"{group['title']} is empty"
        for item in group["items"]:
            assert item["id"] not in ids, f"duplicate id for {item['label']}"
            assert item["label"].strip()
            ids.add(item["id"])
            labels.add(item["label"].lower())
    assert len(ids) == len(labels)


def test_vocab_group_sizes_are_balanced():
    sizes = [len(g["items"]) for g in load("vocab")["groups"]]
    assert sum(sizes) == 733
    assert max(sizes) - min(sizes) <= 1


def test_quant_holds_every_concept_once():
    quant = load("quant")
    labels = [item["label"] for group in quant["groups"] for item in group["items"]]
    assert len(labels) == 162
    assert len(set(labels)) == 162


def test_quant_continuation_rows_are_merged():
    """Rows with an empty Concept cell become extra blocks on the concept above."""
    quant = load("quant")
    by_label = {i["label"]: i for g in quant["groups"] for i in g["items"]}

    three = by_label["Three consecutive integers"]
    explanations = [b for b in three["blocks"] if b["label"].startswith("Explanation")]
    assert len(explanations) == 4, "the four notes for this concept should all be there"

    largest = by_label["Largest factor r of factorial n!"]
    kinds = [b["label"] for b in largest["blocks"]]
    assert kinds.count("Example question 1") == 1 and kinds.count("Example question 2") == 1


def test_every_item_has_something_to_reveal():
    """Only the one concept whose sheet row has no explanation may be blockless."""
    blockless = [
        item["label"]
        for deck in ("vocab", "quant")
        for group in load(deck)["groups"]
        for item in group["items"]
        if not item["blocks"]
    ]
    assert blockless == ["Remainder of sums is sum of remainders"]


# --------------------------------------------------------------------------- board


@pytest.mark.parametrize("deck,day", [("vocab", 1), ("vocab", 16), ("quant", 5), ("quant", 16)])
def test_board_shows_groups_one_to_day(deck, day):
    from gre_mountain import decks

    for shuffle in ("none", "within", "all"):
        board = decks.build_board.__wrapped__(deck, day, shuffle)
        assert len(board["columns"]) == day
        on_board = [i["id"] for column in board["columns"] for i in column["items"]]
        expected = [i["id"] for g in load(deck)["groups"][:day] for i in g["items"]]
        assert sorted(on_board) == sorted(expected), f"{shuffle} lost or added items"
        assert set(board["details"]) == set(expected)


def test_shuffle_modes_differ_but_are_stable():
    from gre_mountain import decks

    default = decks.build_board.__wrapped__("quant", 6, "none")
    within = decks.build_board.__wrapped__("quant", 6, "within")
    mixed = decks.build_board.__wrapped__("quant", 6, "all")

    order = lambda board: [i["id"] for c in board["columns"] for i in c["items"]]  # noqa: E731
    assert order(default) != order(within) != order(mixed)
    assert order(within) == order(decks.build_board.__wrapped__("quant", 6, "within"))
    assert order(within) != order(decks.build_board.__wrapped__("quant", 6, "within", 1))

    # "within" keeps each column's membership, "all" deals across columns.
    for column, group in zip(within["columns"], load("quant")["groups"]):
        assert {i["id"] for i in column["items"]} == {i["id"] for i in group["items"]}
    assert [c["title"] for c in mixed["columns"]][0] == "Mixed 1"


# --------------------------------------------------------------------------- storage


def test_local_store_round_trip(tmp_path):
    store = LocalFileStore(profile="tester", directory=tmp_path)
    assert store.load() == storage.empty_document()
    store.save({"version": 1, "marks": {"vocab": {"3": {"v1": "green"}}}, "settings": {}})
    assert store.load()["marks"]["vocab"]["3"]["v1"] == "green"
    assert (tmp_path / "progress-tester.json").exists()


def test_build_store_picks_backend_from_secrets():
    assert build_store({}, "me").__class__.__name__ == "LocalFileStore"
    gist = build_store({"storage": {"gist": {"token": "x"}}}, "me")
    assert gist.__class__.__name__ == "GistStore" and gist.profile == "me"
    supabase = build_store({"storage": {"supabase": {"url": "http://x", "key": "k"}}})
    assert supabase.__class__.__name__ == "SupabaseStore"
    assert build_store({"storage": {"backend": "local", "profile": "p"}}).profile == "p"
    with pytest.raises(StorageError):
        build_store({"storage": {"backend": "gist"}})
    with pytest.raises(StorageError):
        build_store({"storage": {"backend": "nope"}})


# --------------------------------------------------------------------------- merging


def apply_all(document, changes):
    from gre_mountain.progress import _apply

    for change in changes:
        _apply(document, change)
    return document


def test_marks_are_scoped_to_a_day():
    doc = apply_all(
        storage.empty_document(),
        [
            {"kind": "mark", "deck": "quant", "day": 1, "item": "q1", "status": "green"},
            {"kind": "mark", "deck": "quant", "day": 2, "item": "q1", "status": "red"},
        ],
    )
    assert doc["marks"]["quant"] == {"1": {"q1": "green"}, "2": {"q1": "red"}}


def test_changes_from_two_devices_merge():
    """The laptop's delta lands on top of whatever the phone already wrote."""
    phone = apply_all(
        storage.empty_document(),
        [{"kind": "mark", "deck": "vocab", "day": 4, "item": "v1", "status": "green"}],
    )
    laptop_changes = [
        {"kind": "mark", "deck": "vocab", "day": 4, "item": "v2", "status": "red"},
        {"kind": "setting", "deck": "vocab", "key": "day", "value": 4},
    ]
    merged = apply_all(phone, laptop_changes)
    assert merged["marks"]["vocab"]["4"] == {"v1": "green", "v2": "red"}
    assert merged["settings"]["vocab"]["day"] == 4


def test_clearing_a_day_leaves_other_days_alone():
    doc = apply_all(
        storage.empty_document(),
        [
            {"kind": "mark", "deck": "quant", "day": 1, "item": "q1", "status": "green"},
            {"kind": "mark", "deck": "quant", "day": 2, "item": "q2", "status": "green"},
            {"kind": "clear_day", "deck": "quant", "day": 1},
        ],
    )
    assert doc["marks"]["quant"] == {"2": {"q2": "green"}}


def test_unmarking_removes_the_key():
    doc = apply_all(
        storage.empty_document(),
        [
            {"kind": "mark", "deck": "quant", "day": 1, "item": "q1", "status": "green"},
            {"kind": "mark", "deck": "quant", "day": 1, "item": "q1", "status": None},
        ],
    )
    assert doc["marks"]["quant"]["1"] == {}
