#!/usr/bin/env python3
"""The 3 AM Commit Message (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'fix(prod): the 3 AM deploy ate the database, so I rolled it back, apologised to the on-call human, and am now pretending this commit was always the plan'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
