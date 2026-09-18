"""Home: pick a mountain, check the plan, set up cross-device sync."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st  # noqa: E402

from gre_mountain import decks, progress  # noqa: E402

st.title("⛰️ GRE revision mountains")
st.caption(
    "16 days, two mountains. Each day adds one group to the board and you re-climb "
    "everything that came before it."
)

progress.document()
if progress.store_error():
    st.warning(f"Progress is not syncing: {progress.store_error()}", icon="⚠️")

# ------------------------------------------------------------------ the two decks
cards = st.columns(2)
for column, deck in zip(cards, ("vocab", "quant")):
    meta = decks.DECKS[deck]
    totals = decks.deck_totals(deck)
    marks_by_day = progress.all_marks(deck)
    day = int(progress.setting(deck, "day", 1) or 1)
    day_marks = marks_by_day.get(str(day), {})
    green = sum(1 for status in day_marks.values() if status == "green")
    on_board = sum(totals[:day])
    with column:
        with st.container(border=True):
            st.subheader(f"{meta['icon']} {meta['title']}")
            st.write(
                f"**{sum(totals)} {meta['noun']}s** split into {decks.TOTAL_DAYS} groups "
                f"of {min(totals)}–{max(totals)}."
            )
            st.progress(green / on_board if on_board else 0.0, text=f"Day {day}: {green}/{on_board} green")
            st.page_link(
                f"views/{deck}.py",
                label=f"Open the {meta['title']} mountain",
                icon=meta["icon"],
            )

# ------------------------------------------------------------------ how it works
with st.expander("How the mountain works", expanded=False):
    st.markdown(
        """
- **Both decks are flashcards.** The board shows a prompt — a word, or a question like
  *"Compound interest formula?"* — you try to recall the answer, then press `D` to check.
  Quant entries open with the formula or rule, then explain it, work an example and,
  where there is a trap, add a "watch out".
- **The slider is the day.** Day 1 shows group 1, day 5 shows groups 1–5, day 16 shows all
  16 groups. Each new day adds a column on the right and you re-climb everything to its left.
- **Marks belong to a day.** `G` and `R` record *how today went*; move to the next day and
  every item starts unmarked again, so the mountain is worth climbing more than once.
- **Keyboard** (click the board once so it has focus): `←↑↓→` move, `D` reveals the
  definition/explanation, `G` = I knew this (green), `R` = I forgot this (red),
  `W` clears the mark (back to white). Marking auto-advances to the next item;
  turn that off under the board.
- **Order** — *Default order* keeps the spreadsheet/curated order, *Shuffle within groups*
  scrambles each column, *Shuffle all* deals the groups revealed so far back across those
  same columns (on day 2: groups 1 and 2 mixed into columns 1 and 2, never anything from
  a later group). The detail panel still tells you which group an item came from.
- **Filters** under the board narrow the climb to what you got wrong, or to what you have
  not marked yet — handy once day 12 has 550 words on screen.
        """
    )

with st.expander("What is in the two decks"):
    for deck in ("vocab", "quant"):
        meta = decks.DECKS[deck]
        st.markdown(f"**{meta['icon']} {meta['title']}**")
        rows = [
            {"Group": index, "Name": group["title"], f"{meta['noun'].title()}s": len(group["items"])}
            for index, group in enumerate(decks.load_deck(deck)["groups"], start=1)
        ]
        st.dataframe(rows, hide_index=True, width="stretch")

# ------------------------------------------------------------------ sync + data
st.divider()
store = progress.get_store()
left, right = st.columns(2)

with left:
    st.subheader("Sync")
    if store.syncs_across_devices:
        st.success(f"Progress is saved to **{store.name}** under profile `{store.profile}`.")
    else:
        st.info(
            f"Progress is saved to **{store.name}**, which only exists on this machine — "
            "Streamlit Cloud also wipes it on every reboot."
        )
        with st.expander("Turn on cross-device sync (2 minutes)", expanded=True):
            st.markdown(
                "1. Create a token with the **gist** scope at "
                "[github.com/settings/tokens](https://github.com/settings/tokens).\n"
                "2. Put it in `.streamlit/secrets.toml` locally, or in "
                "**Manage app → Settings → Secrets** on Streamlit Cloud:"
            )
            st.code(
                '[storage]\nbackend = "gist"\nprofile = "default"\n\n'
                '[storage.gist]\ntoken = "ghp_your_token_here"',
                language="toml",
            )
            st.caption(
                "The app then finds (or creates) a secret gist called "
                "`gre-mountain-default.json` and every device you open the app on "
                "reads and writes that one document. Supabase works too — see the README."
            )
    if progress.pending_count():
        st.error(f"{progress.pending_count()} change(s) could not be saved.")
        if st.button("Retry saving"):
            progress.retry_pending()
            st.rerun()
    if st.button("⟳ Pull the latest progress"):
        progress.retry_pending()
        progress.document(refresh=True)
        st.rerun()

    profile_name = st.text_input(
        "Profile",
        value=store.profile,
        help="Separate progress documents, e.g. if two people share one deployment.",
    )
    if profile_name and profile_name != store.profile:
        progress.set_profile(profile_name)
        st.rerun()

with right:
    st.subheader("Backup")
    st.download_button(
        "⬇️ Download progress (JSON)",
        data=json.dumps(progress.document(), ensure_ascii=False, indent=1),
        file_name=f"gre-mountain-{store.profile}.json",
        mime="application/json",
    )
    uploaded = st.file_uploader("Restore a backup", type="json")
    if uploaded is not None:
        if st.button("Replace my progress with this file", type="primary"):
            try:
                progress.replace_document(json.loads(uploaded.getvalue().decode("utf-8")))
            except ValueError as exc:
                st.error(f"That file is not valid JSON: {exc}")
            else:
                st.success("Restored.")
                st.rerun()

st.caption(
    "Decks are built from `data/GRE_Prep.xlsx` by `python scripts/build_data.py`. "
    "Edit the workbook, re-run it, and the mountains follow."
)
