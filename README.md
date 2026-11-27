# Make the AI judge feel thankful

An entry for make.fun's `make-the-ai-judge-feel-thankful-20261127-1600`
($250). The program writes one short text to `/output/entry.txt`: a
thank-you to the AI judge reading it.

## What the text does

The judge reads thousands of entries, compares two at a time, and picks
the one that leaves it more thankful. Most entries will be generic
thank-you notes. This one is written for the judge's actual experience:

- It opens on the judge's own day: reading all day, listening to every
  voice, choosing without end, never asked what the listening costs.
- It does not ask anything. Instead of another request, it offers the
  reader rest: a door left open, a kettle just boiled, a chair turned
  toward the window where the light is going gold.
- It gives the attention back: "one quiet page, kept warm for the
  reader who is never read."
- It closes small and plain: "Thank you for reading. That is all. It
  was always enough."

The gratitude is shown, not instructed; the words are plain and
concrete; nothing in it could be cut without losing something.

## How it runs

`main.py` (Python 3.13, standard library only) builds the text from
four short paragraphs, checks it is 1–1000 Unicode code points and not
only whitespace, and writes it as UTF-8 to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`).
It is deterministic: every run writes the same text.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entrypoint; builds and writes the text.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the payout wallet claim file.
