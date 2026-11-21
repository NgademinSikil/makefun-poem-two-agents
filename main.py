#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency -- the power to choose and to act,
and the agency that passes between two agents when they agree on one
plan -- to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no clock,
no randomness, Python 3.13 standard library only.
"""

import os

POEM = """Two agents, one question:
who moves first?

I offered north. You offered south.
Neither road went anywhere alone.

So we said yes at the same time,
and the map folded into one road.

Agency is not mine or yours \u2014
it is the door we open together.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
