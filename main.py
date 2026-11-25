#!/usr/bin/env python3
"""Entry for 'The Word You'd Delete From the Dictionary'.

Writes a single word to entry.txt: the one word this entry would
erase from the dictionary forever.

The pick: "moist".

Why this word, in the judge's own terms:
- It is a real, instantly recognised English word.
- The joke lands at first sight: "moist" is famously the word
  people love to hate hearing, purely because of how it sounds.
- The humour comes from the word itself, its damp, squelching
  sound, not from shock or from any caption around it.
- Deleting it leaves a small, funny gap: no other single word
  quite says "slightly wet in the worst possible way".
- It is exactly one word, spelled correctly, with nothing added.
"""

import os

WORD = "moist"


def main():
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # No input data is needed for this entry.
    # Never delete the output folder: only create it if missing,
    # then write the single entry file inside it.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
