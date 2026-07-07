## 10 - Hot Potato

## What you will learn

In this exercise you will simulate a game with a queue.
It is a practical way to apply FIFO rotation in rounds.

## What you need to implement

Implement the function `hot_potato(players, passes)`.

Rules:

- Use a queue to rotate players.
- In each round, rotate `passes` times:
	- remove front
	- enqueue at the end
- After rotating, remove the player at the front.
- Repeat until only 1 player remains.
- Return the winner.

## Step-by-step guide

1. Load all players into a queue.
2. While more than one player remains:
	 - rotate `passes` times.
	 - eliminate one player from front.
3. Return the last remaining player.
4. Save the required call result in `winner`.

## Quick example

With `players = ["Ana", "Luis", "Mia", "Leo"]` and `passes = 2`:

- Each round performs 2 rotations.
- Then one front player is removed.
- Process ends with one final winner.

## Note

Each rotation keeps relative order, only moving front to back.

## Required variables

- `winner`: result of `hot_potato(["Ana", "Luis", "Mia", "Leo"], 2)`
