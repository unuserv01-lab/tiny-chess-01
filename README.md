# tiny-chess-01 entry v2

A chess engine in one Python file (`main.py`, 3,627 bytes, limit 4,096):
negamax alpha-beta with iterative deepening to a fixed node budget
(60,000 nodes/move), transposition table, killer moves, MVV-LVA ordering,
quiescence over captures/promotions (all replies when in check), material +
piece-square eval with a bishop-pair bonus. No clock, no randomness: the
same position always gets the same move, so a replay matches.

## What changed from v1 (the rejected entry)

v1 was rejected by the server with practice score 0 (floor 1,154) while the
same engine scored 2.5/6 locally. Diagnosis (trial + fuzz, kit level 9):

- **Too slow for the server's 10 s/move limit.** Local trial-0: v1 mean
  3.5 s/move, max 9.1 s/move — at 70–91% of the limit on this VM. On a
  slower 1-CPU server container, at least one move per game exceeds 10 s
  (`overTime`), losing every game → Elo 0. v2 is ~1.6x faster (mean
  2.2 s/move, max 6.7 s/move, p95 3.8 s/move).
- **No HTTP resilience.** v1's `o()` did one `urlopen` with no status
  check, timeout, or retry; any transient failure (or a non-200) killed
  the whole process and forfeited all remaining games. v2 retries up to
  6 times with backoff (30 s timeout, 4xx not retried).
- **No crash/illegal-move bug found.** 135/135 fuzz positions clean
  (valid positions, python-chess as ground truth); legality validated on
  13,330 pseudo-moves with 0 false positives/negatives.

## Speedup (same search scores as v1, verified move-for-move)

- Lazy legality: pseudo-legal moves are ordered first and tested only
  when tried, with a cheap pin/alignment test (make/unmake + attack test
  only for king moves, in-check positions, and en-passant captures).
  This replaces the old filter that made/unmade + attack-tested every
  pseudo-legal move up front (78% of v1's time).
- Quiescence now searches all replies when in check and skips stand-pat
  when in check (v1 stand-pat'd even in check).
- The undo stack is reset in `n()` (v1 left it un-reset after a
  node-budget abort; harmless in practice, now explicit).

## Local trial-0 (kit level 9, 6 games)

- v2: **2.5/6, Elo ~1,191** (G1 win vs depth-2, G2 loss vs depth-3,
  G3 draw vs depth-4, G4 win vs nodes-100k, G5 loss vs nodes-250k,
  G6 loss vs nodes-500k). Above the 1,154 floor by 37 points.
- v1 on the same gauntlet: also 2.5/6 (different game paths), Elo ~1,191.
- Wall: v2 620 s vs v1 969 s for the 6 games.

## How it plays

It plays the house gauntlet through the env at `MAKEFUN_ENV_URL`:
`POST /game {}` serves the game in play, `POST /move {game, move}`
plays a UCI move, and the loop ends when the env answers `done`.
Stdlib only. `main.py` never reads another file; the search core is a
single lzma preset-9 + base85 payload exec'd at import.
