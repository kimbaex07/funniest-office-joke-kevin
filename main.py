"""The Funniest Office Joke — make.fun entry.

Writes the single-line joke to entry.txt in MAKEFUN_OUTPUT_DIR.
Pure Python 3 standard library only. Deterministic, no network.
"""

import os

JOKE = (
    "I finally figured out why our printer only jams on deadline day: "
    "it's not broken \u2014 it's the only thing in this office with boundaries."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
