"""Entry point: three pages sharing one sidebar."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st  # noqa: E402

st.set_page_config(
    page_title="GRE revision mountains",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="auto",
)

navigation = st.navigation(
    [
        st.Page("views/home.py", title="Home", icon="⛰️", default=True),
        st.Page("views/vocab.py", title="Vocab", icon="📘"),
        st.Page("views/quant.py", title="Quant", icon="📐"),
    ]
)
navigation.run()
