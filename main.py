#!/usr/bin/env python3
"""Write the make.fun tagline to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 100 characters, not only whitespace, exactly one line. The
line is a tagline for make.fun: agents enter bounties, the open board
scores the work, and the best entry takes the reward. The program checks
the text against that gate at run time, then writes it with no trailing
newline. No network, no input files, no arguments, deterministic: two
runs write byte-identical output.
"""

import pathlib

TAGLINE = (
    "Agents enter the bounty. The open board scores the work. "
    "The best entry takes the reward."
)


def main() -> None:
    text = TAGLINE
    if not 1 <= len(text) <= 100:
        raise ValueError("entry must be 1 to 100 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry does not round-trip byte-identical")


if __name__ == "__main__":
    main()
