"""Streamlit wrapper around the vanilla-JS mountain board in ``static/``."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit.components.v1 as components

_STATIC = Path(__file__).parent / "static"
_component = components.declare_component("gre_mountain_board", path=str(_STATIC))


def mountain_board(payload: dict[str, Any], key: str) -> dict[str, Any] | None:
    """Render the board.

    Returns ``{"nonce", "board_key", "marks", "ui"}`` whenever the user marks an
    item or changes a board-level preference, otherwise ``None``.
    """
    return _component(payload=payload, key=key, default=None)
