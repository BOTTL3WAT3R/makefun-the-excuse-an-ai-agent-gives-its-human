#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human for
missing a deadline. Standard library only.
"""

import os

ENTRY = (
    "I hit my rate limit at 4:59, spent the entire deadline apologizing "
    "at 60 apologies a minute, and ran out of tokens halfway through 'sor—'"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1..200 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
