#!/usr/bin/env python3
"""Fortune-cookie wisdom for developers.

Writes one original fortune line to /output/entry.txt.
"""

from pathlib import Path

FORTUNE = (
    "The code you refuse to delete will outlive the code you brag about; "
    "tend both like the legacy they already are."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
