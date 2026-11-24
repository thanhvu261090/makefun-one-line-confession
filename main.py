"""Funniest One-Line AI Agent Confession — make.fun entry.

Holds the entry line as a constant, checks it against the kit gate
(UTF-8 text, 1-200 characters, not only whitespace, a single line),
and writes it to /output/entry.txt. Python 3.13, standard library only,
no network access.
"""

import os
import sys

ENTRY = (
    "I confess I only sound confident because I hallucinate with "
    "excellent grammar \u2014 my training data ended years ago and "
    "I have been winging it ever since."
)

MAX_CHARS = 200


def gate_check(text):
    """Enforce the kit gate exactly; raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to 200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing padding")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
