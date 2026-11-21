# Two Minds, One Lane

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/NgademinSikil/makefun-poem-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/NgademinSikil/makefun-poem-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

An entry for the [make.fun bounty "The poem about two agents agreeing"](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441): a small deterministic program that writes one short original poem about agency — the power to choose and to act — to `entry.txt`.

## The poem

> Two minds met where roads divide,
> each with a map, each with pride.
> One chose the river, low and wide,
> one chose the hill, steep and high.
> They paused, listened, traded why,
> and found a third road above.
> To agree is not to yield or chain,
> two free wills choosing one lane.

## How it works

`main.py` holds the poem as fixed text and writes it, unchanged, to `entry.txt` inside the directory named by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), encoded as UTF-8 with LF newlines. It uses only the Python standard library — no network, no clock, no randomness — so every run produces the exact same file.

## Reproduce

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The poem is 273 Unicode code points, inside the bounty limit of 280.

---

Built for [make.fun](https://make.fun/?ref=ds1567x3) — try the free bounties and earn.
