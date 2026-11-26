#!/usr/bin/env python3
"""Rename the Planet entry.

Writes one line renaming Earth and saying why, to entry.txt under
MAKEFUN_OUTPUT_DIR (default /output). Stdlib only.
"""

import os
import sys

PLANET = "Earth"
NEW_NAME = "The Airbnb"
LINE = (
    "Earth is now 'The Airbnb' \u2014 8 billion guests, nobody does the "
    "dishes, and the host hasn't replied in 4.5 billion years."
)

MAX_CHARS = 200


def build_line():
    text = LINE.strip()
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry length %d outside 1-%d" % (len(text), MAX_CHARS)
        )
    if PLANET not in text or NEW_NAME not in text:
        raise ValueError("entry must name the planet and its new name")
    if "\u2014" not in text:
        raise ValueError("entry must join the new name to its why")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    return text


def main():
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise ValueError(
            "cannot create output directory %r: %s" % (out_dir, exc)
        ) from exc
    if not os.path.isdir(out_dir):
        raise ValueError("output path %r is not a directory" % out_dir)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(target, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != line:
        raise ValueError("read-back mismatch")
    print("wrote %d characters to %s" % (len(saved), target))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
