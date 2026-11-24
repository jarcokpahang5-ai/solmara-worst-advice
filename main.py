"""Worst AI Advice -- make.fun entry.

Holds one line of the worst possible advice an AI could give, at most
140 characters. The program checks the line, prints it, and writes it
to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
Revised 2026-11-24: refactored the output write into write_entry().
"""

import os

ADVICE = (
    "Your production database is slow, so delete it: a fresh start is "
    "always faster than debugging."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def check_advice(text):
    """Keep the advice to one non-blank line of at most 140 characters.

    Raises ValueError when the text is not a string, spans more than
    one line, is blank, or exceeds the 140-character limit.
    """
    if not isinstance(text, str):
        raise ValueError("advice must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("advice must be a single line")
    if not text.strip():
        raise ValueError("advice must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "advice is %d characters, over the 140 limit" % len(text)
        )
    return text


def write_entry(line):
    """Write the checked advice line to the entry file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    line = check_advice(ADVICE)
    print(line)
    write_entry(line)


if __name__ == "__main__":
    main()
