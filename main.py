"""Say What Actually Broke - one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt:
the brutal truth about a real failure, told plainly, with a laugh.
"""

import os

ENTRY = (
    "Error 503: our security certificate expired because the renewal "
    "reminder went to an employee who left in 2023. Nothing was hacked. "
    "A calendar lost to an empty chair."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
