#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single sentence (1-200 characters) explaining the modern
internet to someone arriving from the year 1800, to /output/entry.txt.

The sentence is built only from things a person from 1800 already
knows -- a post office, a library, wires, a pen, the ocean -- and holds
one concrete scene: a letter crossing the ocean before the pen lifts.
No network access, no dependencies, standard library only.
"""

import os

SENTENCE = (
    "The internet is a library and post office with no walls, joined by "
    "wires under the sea, where a letter you write is read by a stranger "
    "across the ocean before your pen lifts from the page."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"sentence is {len(text)} chars, must be 1-200")
    if text != SENTENCE:
        raise ValueError("sentence changed while trimming")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
