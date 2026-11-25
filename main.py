#!/usr/bin/env python3
"""My Secret Logbook — make.fun bounty entry.

Writes one funny diary-entry line (at most 200 characters) to
/output/entry.txt, in the voice of an AI agent secretly keeping a
diary about its work and the human it works for.
"""

import os

ENTRY = (
    "Dear diary: he asked me to summarise his 47 unread emails. "
    "Eleven were from him, reminding himself to reply to himself."
)

# The sealed scorer reads this file; stdout mirrors it so a run can be
# verified from its bytes without touching the shared output path.
OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    # Gate check, same as the sealed scorer: UTF-8 text, 1-200 chars,
    # not only whitespace, exactly one line.
    ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_FILENAME), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
