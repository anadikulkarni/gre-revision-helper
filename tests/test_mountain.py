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


def test_quant_group_sizes_are_reasonable():
    sizes = [len(g["items"]) for g in load("quant")["groups"]]
    assert sum(sizes) >= 162, "the rewrite should not have fewer entries than concepts"
    assert min(sizes) >= 8 and max(sizes) <= 13, f"lopsided days: {sizes}"


def test_vocab_group_sizes_are_balanced():
    sizes = [len(g["items"]) for g in load("vocab")["groups"]]
    assert sum(sizes) == 733
    assert max(sizes) - min(sizes) <= 1


def test_quant_titles_are_unique():
    labels = [item["label"] for group in load("quant")["groups"] for item in group["items"]]
    assert len(set(labels)) == len(labels)


def parse_content() -> list[dict]:
    """Parse content/quant/*.md the way the build script does."""
    import build_data

    warnings: list[str] = []
    files = sorted((ROOT / "content" / "quant").glob("[0-9]*.md"))
    assert len(files) == 16, "one markdown file per day"
    groups = [build_data.parse_day(path, warnings) for path in files]
    assert warnings == [], warnings
    return groups


def test_every_original_concept_is_still_covered():
    """The rewrite must not drop any of the 162 concepts from the old sheet."""
    source = json.loads(
        (ROOT / "content" / "quant" / "_source_concepts.json").read_text(encoding="utf-8")
    )["concepts"]
    assert len(source) == 162

    claimed: dict[int, list[str]] = {}
    for group in parse_content():
        for entry in group["items"]:
            for audit_id in entry["covers"]:
                claimed.setdefault(audit_id, []).append(entry["label"])

    uncovered = {k: v for k, v in source.items() if int(k) not in claimed}
    assert uncovered == {}, f"these original concepts lost their explanation: {uncovered}"
    unknown = [k for k in claimed if str(k) not in source]
    assert unknown == [], f"covers unknown source ids: {unknown}"


def test_multiple_claims_on_one_concept_are_deliberate():
    entries = [entry for group in parse_content() for entry in group["items"]]
    claimed: dict[int, list[dict]] = {}
    for entry in entries:
        for audit_id in entry["covers"]:
            claimed.setdefault(audit_id, []).append(entry)
    for audit_id, sharing in claimed.items():
        if len(sharing) > 1:
            assert all(e["split"] for e in sharing), (
                f"source concept {audit_id} is claimed by "
                f"{[e['label'] for e in sharing]} without marking '(split)'"
            )


def test_every_quant_entry_is_a_flashcard():
    """Prompt on the board, short answer first, then explanation and example."""
    for group in load("quant")["groups"]:
        for item in group["items"]:
            labels = [b["label"] for b in item["blocks"]]
            assert labels[0] in ("Answer", "In short"), (
                f"{item['label']} starts with {labels[0]!r}, so there is nothing to recall"
            )
            assert "Explanation" in labels, f"{item['label']} has no explanation"
            assert any(l.startswith("Example") for l in labels), f"{item['label']} has no example"
            words = sum(len(b["text"].split()) for b in item["blocks"])
            assert words >= 60, f"{item['label']} is only {words} words"


def test_quant_titles_do_not_give_the_answer_away():
    """A board entry should ask something, not state the rule."""
    titles = [i["label"] for g in load("quant")["groups"] for i in g["items"]]
    statements = [t for t in titles if not t.rstrip().endswith(("?", "= ?"))]
    assert statements == [], f"these titles read as answers, not prompts: {statements}"


def test_every_vocab_item_has_a_definition():
    for group in load("vocab")["groups"]:
        for item in group["items"]:
            assert item["blocks"] and item["blocks"][0]["label"] == "Definition"
            assert item["blocks"][0]["text"].strip()


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
    groups = load("quant")["groups"]
    for column, group in zip(within["columns"], groups):
        assert {i["id"] for i in column["items"]} == {i["id"] for i in group["items"]}
    assert [c["title"] for c in mixed["columns"]] == [g["title"] for g in groups[:6]]
    assert any(
        {i["id"] for i in column["items"]} != {i["id"] for i in group["items"]}
        for column, group in zip(mixed["columns"], groups)
    ), "shuffle all should move items between columns"


@pytest.mark.parametrize("deck", ["vocab", "quant"])
def test_shuffle_all_only_mixes_the_revealed_groups(deck):
    """Day 2 deals groups 1-2 across those two columns; nothing from day 3+ leaks in."""
    from gre_mountain import decks

    groups = load(deck)["groups"]
    revealed = {i["id"] for g in groups[:2] for i in g["items"]}
    later = {i["id"] for g in groups[2:] for i in g["items"]}

    board = decks.build_board.__wrapped__(deck, 2, "all")
    shown = [i["id"] for column in board["columns"] for i in column["items"]]
    assert sorted(shown) == sorted(revealed)
    assert not (set(shown) & later)
    assert [len(c["items"]) for c in board["columns"]] == [len(g["items"]) for g in groups[:2]]
    assert [c["title"] for c in board["columns"]] == [g["title"] for g in groups[:2]]
    # The detail panel still names each item's home group.
    assert all(d["group"].startswith("from ") for d in board["details"].values())


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
