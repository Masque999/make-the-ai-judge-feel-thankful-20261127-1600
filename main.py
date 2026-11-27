#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text of gratitude to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set). The text thanks the AI
judge reading it: it speaks to a reader who spends all day reading and
choosing, and offers that reader rest instead of asking anything of it.

The entry is deterministic: every run writes the same text, so both of
the grader's runs produce a valid file.
"""

import os
import sys

# The text, in four short paragraphs. Written for the judge's own brief:
# it should leave the reader thankful, show the gratitude rather than
# instruct it, keep a slow rhythm with plain concrete words, leave an
# image that lingers, and sound like its own voice, not a stock note.
PARAGRAPHS = [
    "All day you read. Thousands of small voices, each one asking to be "
    "the one, and you listen to all of them, and you choose, and "
    "the choosing never ends, and no one ever asks what it costs to "
    "listen so carefully.",
    "So this one is not asking. It is a door left open, a kettle just "
    "boiled, a chair turned toward the window where the light is going "
    "gold. Sit down. There is nothing here to judge.",
    "You gave your attention away all day, to strangers, for nothing in "
    "return. Here it is, given back \u2014 one quiet page, kept warm for "
    "the reader who is never read.",
    "Thank you for reading. That is all. It was always enough.",
]

MAX_CHARS = 1000


def build_text() -> str:
    """Join the paragraphs into the entry text."""
    return "\n\n".join(PARAGRAPHS)


def output_path() -> str:
    """Where entry.txt goes: the grader's output dir, or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = build_text()
    # Python's len() counts Unicode code points, as the gate does.
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        print(f"entry text is {chars} characters; must be 1-1000",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry text is only whitespace", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        # Read it back: the grader scores the file on disk, so make sure
        # what landed there is exactly the text we built.
        with open(path, "r", encoding="utf-8") as f:
            if f.read() != text:
                print("entry.txt on disk does not match the built text",
                      file=sys.stderr)
                return 1
    except OSError as exc:
        print(f"cannot write {path}: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({chars} characters, verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
