"""Shared page chrome for the two mountains."""

from __future__ import annotations

from typing import Any

import streamlit as st

from . import decks, progress
from .component import mountain_board

UI_DEFAULTS = {"filter": "all", "alwaysDef": False, "autoAdvance": True}


def _inject_css() -> None:
    st.markdown(
        """
        <style>
          .block-container {padding-top: 2.2rem; padding-bottom: 0.6rem;}
          div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"] {display: none;}
          .mountain-day {text-align: center; font-size: 1.35rem; font-weight: 700; line-height: 2.1rem;}
          .mountain-sub {text-align: center; color: #7a869c; font-size: 0.85rem; margin-top: -0.4rem;}
          /* On a phone Streamlit gives every column its own full-width row, which
             pushes the board off screen. Keep the chrome to two tidy rows instead:
             the slider replaces the day arrows and the board shows its own tally. */
          @media (max-width: 640px) {
            .block-container {padding-left: 0.6rem; padding-right: 0.6rem; padding-top: 3.4rem;}
            .mountain-day {font-size: 1.05rem; line-height: 1.5rem;}
            .mountain-sub {font-size: 0.75rem;}
            .st-key-mountain-dayhdr div[data-testid="stColumn"]:not(:nth-child(3)) {display: none;}
            .st-key-mountain-toolbar div[data-testid="stHorizontalBlock"] {gap: 0.35rem !important;}
            .st-key-mountain-toolbar div[data-testid="stColumn"]:nth-child(1) {min-width: 100% !important;}
            .st-key-mountain-toolbar div[data-testid="stColumn"]:nth-child(2),
            .st-key-mountain-toolbar div[data-testid="stColumn"]:nth-child(3),
            .st-key-mountain-toolbar div[data-testid="stColumn"]:nth-child(4) {
              min-width: 30% !important; flex: 1 1 30% !important;
            }
            .st-key-mountain-toolbar div[data-testid="stColumn"]:nth-child(5) {display: none;}
            .st-key-mountain-toolbar button {padding-left: 0.3rem; padding-right: 0.3rem;}
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _day_key(deck: str) -> str:
    return f"day_{deck}"


def _step_day(deck: str, delta: int) -> None:
    key = _day_key(deck)
    st.session_state[key] = max(1, min(decks.TOTAL_DAYS, st.session_state[key] + delta))
    progress.set_setting(deck, "day", st.session_state[key])


def _on_day_change(deck: str) -> None:
    progress.set_setting(deck, "day", st.session_state[_day_key(deck)])


def _on_shuffle_change(deck: str) -> None:
    label = st.session_state[f"shuffle_{deck}"]
    mode = next(key for key, text in decks.SHUFFLE_MODES.items() if text == label)
    progress.set_setting(deck, "shuffle", mode)


def render_deck_page(deck: str) -> None:
    meta = decks.DECKS[deck]
    _inject_css()
    progress.document()  # first read of the session pulls whatever other devices saved

    # The board's value from the previous render is already in session_state, so
    # fold it in before drawing anything: the counters below then show live numbers
    # without costing a second rerun (which would re-send the whole board payload).
    _handle_board_result(deck, st.session_state.get(f"board_{deck}"))

    day_key = _day_key(deck)
    if day_key not in st.session_state:
        st.session_state[day_key] = int(progress.setting(deck, "day", 1) or 1)
    st.session_state[day_key] = max(1, min(decks.TOTAL_DAYS, int(st.session_state[day_key])))

    # ---------------------------------------------------------------- day header
    header = st.container(key="mountain-dayhdr")
    spacer_l, left, middle, right, spacer_r = header.columns(
        [3, 0.6, 5, 0.6, 3], vertical_alignment="center"
    )
    with left:
        st.button(
            "◀",
            key=f"prev_{deck}",
            disabled=st.session_state[day_key] <= 1,
            on_click=_step_day,
            args=(deck, -1),
            help="Previous day",
        )
    with right:
        st.button(
            "▶",
            key=f"next_{deck}",
            disabled=st.session_state[day_key] >= decks.TOTAL_DAYS,
            on_click=_step_day,
            args=(deck, 1),
            help="Next day",
        )
    day = st.session_state[day_key]
    with middle:
        groups_label = "group 1" if day == 1 else f"groups 1-{day}"
        st.markdown(
            f"<div class='mountain-day'>{meta['icon']} {meta['title']} &middot; Day {day} of {decks.TOTAL_DAYS}</div>"
            f"<div class='mountain-sub'>{groups_label} on the mountain</div>",
            unsafe_allow_html=True,
        )

    st.slider(
        "Day",
        min_value=1,
        max_value=decks.TOTAL_DAYS,
        key=day_key,
        label_visibility="collapsed",
        on_change=_on_day_change,
        args=(deck,),
    )
    day = st.session_state[day_key]

    # ---------------------------------------------------------------- toolbar
    shuffle = str(progress.setting(deck, "shuffle", "none") or "none")
    if shuffle not in decks.SHUFFLE_MODES:
        shuffle = "none"
    reshuffle_key = f"reshuffle_{deck}"
    st.session_state.setdefault(reshuffle_key, 0)

    bar = st.container(key="mountain-toolbar").columns(
        [2.4, 1.1, 1, 1, 3.5], vertical_alignment="center"
    )
    with bar[0]:
        st.selectbox(
            "Order",
            options=list(decks.SHUFFLE_MODES.values()),
            index=list(decks.SHUFFLE_MODES).index(shuffle),
            key=f"shuffle_{deck}",
            label_visibility="collapsed",
            on_change=_on_shuffle_change,
            args=(deck,),
        )
    with bar[1]:
        if st.button(
            "🔀 Reshuffle",
            key=f"reshuffle_btn_{deck}",
            width="stretch",
            disabled=shuffle == "none",
            help="Draw a new random order",
        ):
            st.session_state[reshuffle_key] += 1
    with bar[2]:
        if st.button(
            "↺ Reset",
            key=f"reset_{deck}",
            width="stretch",
            help=f"Clear every green/red mark made on day {day}",
        ):
            progress.clear_day(deck, day)
            st.rerun()
    with bar[3]:
        if st.button(
            "⟳ Sync",
            key=f"sync_{deck}",
            width="stretch",
            help="Re-read progress saved on your other devices",
        ):
            progress.retry_pending()
            progress.document(refresh=True)
            st.rerun()
    with bar[4]:
        counts = decks.tally(deck, day, progress.marks(deck, day))
        st.markdown(
            f"<div style='text-align:right;padding-top:2px'>"
            f"<b style='color:#2fa360'>{counts['green']}</b> known &middot; "
            f"<b style='color:#e0474c'>{counts['red']}</b> forgot &middot; "
            f"{counts['left']} left of {counts['total']} {meta['noun']}s</div>",
            unsafe_allow_html=True,
        )

    if progress.store_error():
        st.warning(f"Progress is not syncing: {progress.store_error()}", icon="⚠️")

    # ---------------------------------------------------------------- board
    board = decks.build_board(deck, day, shuffle, st.session_state[reshuffle_key])
    ui_state = {
        "filter": progress.setting(deck, "filter", UI_DEFAULTS["filter"]),
        "alwaysDef": bool(progress.setting(deck, "always_definition", UI_DEFAULTS["alwaysDef"])),
        "autoAdvance": bool(progress.setting(deck, "auto_advance", UI_DEFAULTS["autoAdvance"])),
    }
    height = int(progress.setting(deck, "height", 760) or 760)
    board_key = "|".join(
        [
            deck,
            str(day),
            shuffle,
            str(st.session_state[reshuffle_key]),
            str(progress.revision()),
            progress.profile() or "default",
        ]
    )
    payload: dict[str, Any] = {
        "board_key": board_key,
        "columns": board["columns"],
        "details": board["details"],
        "marks": progress.marks(deck, day),
        "ui": ui_state,
        "height": height,
        "column_width": meta["column_width"],
    }

    st.session_state[f"_ctx_{deck}"] = {"key": board_key, "day": day, "ui": ui_state}
    mountain_board(payload, key=f"board_{deck}")

    _render_sidebar(deck, day, height)


def _handle_board_result(deck: str, result: dict[str, Any] | None) -> None:
    """Persist marks / preferences the board sent back on the previous render."""
    context = st.session_state.get(f"_ctx_{deck}")
    if not result or not context or result.get("board_key") != context["key"]:
        return
    nonce_key = f"_nonce_{deck}"
    if result.get("nonce") == st.session_state.get(nonce_key):
        return
    st.session_state[nonce_key] = result.get("nonce")

    day = context["day"]
    ui_state = context["ui"]
    changes = progress.diff_marks(deck, day, result.get("marks") or {})
    incoming_ui = result.get("ui") or {}
    for board_field, setting_name in (
        ("filter", "filter"),
        ("alwaysDef", "always_definition"),
        ("autoAdvance", "auto_advance"),
    ):
        if board_field in incoming_ui and incoming_ui[board_field] != ui_state[board_field]:
            changes.append(
                {
                    "kind": "setting",
                    "deck": deck,
                    "key": setting_name,
                    "value": incoming_ui[board_field],
                }
            )
    if changes:
        progress.apply_changes(changes)


def _render_sidebar(deck: str, day: int, height: int) -> None:
    meta = decks.DECKS[deck]
    with st.sidebar:
        st.markdown(f"### {meta['icon']} {meta['title']} mountain")
        store = progress.get_store()
        if store.syncs_across_devices:
            st.caption(f"Saving to {store.name} · profile `{store.profile}`")
        else:
            st.caption(f"Saving to {store.name} — this device only. See Home for cross-device sync.")
        if progress.pending_count():
            st.error(f"{progress.pending_count()} change(s) not saved yet.")
            if st.button("Retry saving", width="stretch", key=f"retry_{deck}"):
                progress.retry_pending()
                st.rerun()

        st.divider()
        new_height = st.number_input(
            "Board height (px)",
            min_value=420,
            max_value=1600,
            value=height,
            step=40,
            key=f"height_{deck}",
            help="Make the board taller on a big screen, shorter on a phone.",
        )
        if int(new_height) != height:
            progress.set_setting(deck, "height", int(new_height))
            st.rerun()

        st.divider()
        st.markdown("**Progress by day**")
        marks_by_day = progress.all_marks(deck)
        totals = decks.deck_totals(deck)
        rows = []
        for index in range(1, decks.TOTAL_DAYS + 1):
            day_marks = marks_by_day.get(str(index), {})
            green = sum(1 for status in day_marks.values() if status == "green")
            red = sum(1 for status in day_marks.values() if status == "red")
            seen = sum(totals[:index])
            rows.append(
                {
                    "Day": index,
                    "On board": seen,
                    "✅": green,
                    "❌": red,
                }
            )
        st.dataframe(rows, hide_index=True, width="stretch", height=280)

        st.divider()
        if st.button(
            f"Reset all {meta['title']} progress",
            width="stretch",
            key=f"reset_deck_{deck}",
        ):
            st.session_state[f"confirm_reset_{deck}"] = True
        if st.session_state.get(f"confirm_reset_{deck}"):
            st.warning(f"This clears every mark on all {decks.TOTAL_DAYS} days of {meta['title']}.")
            confirm, cancel = st.columns(2)
            if confirm.button("Yes, reset", width="stretch", key=f"confirm_{deck}"):
                progress.clear_deck(deck)
                st.session_state[f"confirm_reset_{deck}"] = False
                st.rerun()
            if cancel.button("Cancel", width="stretch", key=f"cancel_{deck}"):
                st.session_state[f"confirm_reset_{deck}"] = False
                st.rerun()
