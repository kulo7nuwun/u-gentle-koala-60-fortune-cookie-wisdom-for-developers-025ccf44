#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to entry.txt (1-120 characters, UTF-8).
"""

import os
from pathlib import Path

LINE = "The legacy code you curse was once a clever fix on a tired Friday."


def main() -> None:
    # Mirror the competition gate: 1-120 characters, not only whitespace.
    text = LINE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry line is {len(text)} characters, must be 1-120")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
