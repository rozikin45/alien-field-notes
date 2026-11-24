"""Alien Field Notes entry: write one fixed one-line alien tourist review of Earth.

The review is a constant string, so the program is fully deterministic:
no randomness, no clock, no network. Every run writes the exact same
131 characters to entry.txt in the output directory.

The line: an alien tourist's review with a split verdict (five stars for
the views, one star for the gift shop), one clean joke from the alien's
angle (the shop sells tiny models of the reviewer's own ship and calls
them "UFOs"), and a real-review closing ("Would visit again.").
"""

import os
from pathlib import Path

REVIEW = "Five stars for the views, one star for the gift shop: it sells tiny models of my own ship and calls them 'UFOs.' Would visit again."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(REVIEW, encoding="utf-8")
