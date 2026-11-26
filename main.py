#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one line — the funniest single-line diagnosis an AI therapist
hands its human — to /output/entry.txt.
"""

import os

ENTRY = "Diagnosis: acute main-character syndrome complicated by chronic doomscrolling. Prescription: touch grass twice daily — and stop Googling your symptoms at 3 a.m., you're scaring the algorithm."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError unless text is a single non-empty line within the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters, got {len(text)}")


def main() -> int:
    validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    validate(written)
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
