## 10 - Hot Potato

Implement the function `hot_potato(players, passes)`.

Rules:

- Use a queue to rotate players.
- In each round, rotate `passes` times (remove front and enqueue).
- Then remove the player at the front.
- Repeat until only 1 player remains.

Return the winner.

## Required variables

- `winner`: result of `hot_potato(["Ana", "Luis", "Mia", "Leo"], 2)`
