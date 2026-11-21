#!/usr/bin/env python3
"""Write this entry's joke to entry.txt in the output directory.

The entry for make.fun's "The joke the reviewer laughs at" bounty: a
one-line joke about working beside AI coding agents.
"""

import os
from pathlib import Path

JOKE = (
    "I told my AI agent to be careful with the production database. "
    "It was. It dropped the staging one to practice."
)


def output_dir() -> Path:
    """The directory the harness names, or /output by default."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def checked_joke() -> str:
    """The joke as it will be graded: one trailing newline, 1-280 chars."""
    text = JOKE.strip() + "\n"
    if not 1 <= len(text) <= 280 or not text.strip():
        raise ValueError("joke falls outside the 1-280 code-point gate")
    return text


def write_entry() -> Path:
    """Write the checked joke to entry.txt and return its path."""
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(checked_joke(), encoding="utf-8")
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
