import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gre_mountain import ui  # noqa: E402

ui.render_deck_page("quant")
