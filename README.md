# tiny-chess-01 entry

A chess engine in one Python file (`main.py`, at most 4,096 bytes):
negamax alpha-beta with iterative deepening to a fixed node budget,
transposition table, killer moves, MVV-LVA ordering, quiescence over
captures/promotions and replies to check, material + piece-square eval
with a bishop-pair bonus. No clock, no randomness: the same position
always gets the same move, so a replay matches.

It plays the house gauntlet through the env at `MAKEFUN_ENV_URL`:
`POST /game {}` serves the game in play, `POST /move {game, move}`
plays a UCI move, and the loop ends when the env answers `done`.
