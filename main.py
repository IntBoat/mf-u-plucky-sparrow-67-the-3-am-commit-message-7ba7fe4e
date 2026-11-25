#!/usr/bin/env python3
"""The 3 AM Commit Message — a make.fun one-line entry."""

from pathlib import Path

ENTRY = "fix(prod): the 3 AM deploy ate the database, so I apologised to the logs and pushed anyway"

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
