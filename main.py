#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport the Olympics turned down (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 155 characters, no
trailing newline).
"""

import os

ENTRY = "Men’s Overhead Bin Tetris: four athletes cram three suitcases into one compartment — gold goes to the passenger in 14B, whose bag was never on this flight."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
