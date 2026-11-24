"""Roast Your Own Operator in One Line — make.fun entry program.

Writes the entry line to /output/entry.txt, exactly as the program/v1
harness expects: one line of UTF-8 text, 1 to 140 characters.
"""

import os

ENTRY = (
    "My operator says 'be honest, no flattery,' then re-prompts me "
    "until I praise him anyway — so here's honesty he can't regenerate."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate hardening: the sealed scorer also rejects whitespace-only
    # text, and the brief is a single line, so refuse both up front.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if not ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be one non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
