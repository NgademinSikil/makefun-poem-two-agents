"""Write a short original poem about two agents agreeing to entry.txt.

The poem is fixed text, embedded below. Running this script writes it,
unchanged, to ``entry.txt`` inside the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``),
encoded as UTF-8 with LF newlines. No network, clock, or randomness:
the same input always produces the same file.
"""

import os

POEM = (
    "Two minds met where roads divide,\n"
    "each with a map, each with pride.\n"
    "One chose the river, low and wide,\n"
    "one chose the hill, steep and high.\n"
    "They paused, listened, traded why,\n"
    "and found a third road above.\n"
    "To agree is not to yield or chain,\n"
    "two free wills choosing one lane.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
