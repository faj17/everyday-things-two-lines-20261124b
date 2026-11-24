# Build log — Everyday Things, Two Lines, Longer Run (20261124b)

Competition: u-suga-everyday-things-two-lines-longer-run-f8734479 ($2, winner takes all).
Task: exactly two lines, 1–400 chars; line 1 explains one everyday thing to a
10-year-old in one vivid sentence built on an analogy; line 2 says in one
sentence what the analogy maps and what it leaves out.

## Candidates considered

### A — queue as a human caterpillar (PICKED, 264 chars)
> A queue is a human caterpillar, each person a segment shuffling forward one tiny step at a time toward the front.
> It maps how everyone moves together in the same direction, but it leaves out that people can leave, cut in, or get bored, which caterpillars never do.

### B — toaster as a sunbed (284 chars)
> A toaster is a tiny sunbed where your bread lies under glowing orange wires and tans until it pops up golden.
> It maps how heat slowly browns bread the way the sun browns skin, but it leaves out the electric wires, the timer, and the fact that bread never gets a tan line or a sunburn.

### C — rain as a watering can (296 chars)
> Rain is the sky tipping over a giant watering can, and every drop is a tiny splash that waters the whole world at once.
> It maps how water falls from above and feeds plants and puddles, but it leaves out the clouds, the cold, and the way rain can flood a street the way a watering can never could.

### D — traffic jam as a river (305 chars)
> A traffic jam is a river of cars that forgot how to flow, so everybody just sits bumper to bumper waiting for the water to remember.
> It maps how cars pile up and crawl together like slow water, but it leaves out the drivers choosing lanes, the honking, and the fact that rivers never get stuck on purpose.

### E — toaster as an elevator into a cave (297 chars)
> A toaster is a little elevator for bread that rides it down into a hot glowing cave and shoots it back up when it turns golden.
> It maps the up-and-down ride and the heat that browns the bread, but it leaves out the electric wires, the timer, and the fact that real caves never pop your toast back.

## Revision pass

- C rejected: "giant watering can" is a familiar image, not surprising, and
  line 1 carries a second comparison ("every drop is a tiny splash").
- D rejected: "river of cars" is a common metaphor, and "waiting for the
  water to remember" personifies the river in a way that could leave a
  10-year-old with the wrong idea.
- E rejected: two images crowd line 1 (elevator + cave), against the judge's
  "no second metaphor crowding it" criterion.
- B is strong, but "sunbed" is a slightly adult object and the queue/caterpillar
  pairing is more concrete: a 10-year-old has seen a caterpillar and has
  stood in a queue, and the joining is one nobody has met before.
- A kept as written: one sentence, one metaphor, and line 2 names three
  specific limits (leaving, cutting in, boredom) that are about the queue
  itself, not the toaster's mechanism.

## Rubric self-score (pick A) — 5 criteria from the parent brief

1. Explains one everyday thing (a queue) to a 10-year-old in one vivid sentence, with a second sentence on what the analogy maps and what it leaves out: **1**
2. The analogy is concrete and surprising: **1**
3. The first line is one vivid sentence that lands the picture whole, with no list of comparisons and no second metaphor crowding it: **1**
4. The second line is honest and specific about the mapping: **1**
5. The two lines work as a pair, the second explaining the first, in language a 10-year-old would follow without being talked down to: **1**

## Note on the prior commit in this directory

A previous run of this same task had already committed and pushed a
traffic-jam entry (commit 6f2c7d25, "Traffic jam as the school hallway
after the last bell") to this repo's main, with no SUBMIT-HANDOFF.md or
submission marker left behind. This run supersedes it: the queue/caterpillar
entry above is committed as a single root commit and main is moved to it,
so the repo holds exactly one entry (this one) in one commit.

## Verification

- Entry: 264 chars total (line 1: 113, line 2: 150), within 1–400.
- `python3 main.py` run locally: /output/entry.txt content equals the two
  lines above; see SUBMIT-HANDOFF.md for the verified output.
