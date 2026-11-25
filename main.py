#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single one-line joke about a meeting that should have been an
email to /output/entry.txt (1-200 characters, plain UTF-8 text, one line).

The joke: the meeting's entire content already existed as an email --
"per my last email" -- and the six people in the room had not even read
it. The turn lands on the last words.
"""

import os

LINE = (
    'The meeting was "per my last email" read aloud, slowly, '
    "by six people who hadn't read it."
)


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
