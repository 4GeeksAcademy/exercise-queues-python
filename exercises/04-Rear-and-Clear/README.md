## 04 - Rear and Clear

## What you will learn

In this exercise you will inspect the last element and reset a queue.
These are common operations when you need queue status and a clean restart.

## What you need to implement

Add to `Queue`:

- `rear()`: returns the last element without removing it.
- `clear()`: empties the whole queue.

If `rear()` is called on an empty queue, return `None`.

## Step-by-step guide

1. In `rear()`, check if there are elements.
2. If there are elements, return `self.items[-1]`.
3. If there are no elements, return `None`.
4. In `clear()`, empty the queue.
5. Create `queue` with 1, 2, and 3.
6. Save `last_item` before clearing.
7. Run `clear()` and then save `size_after_clear`.

## Quick example

With queue `[1, 2, 3]`:

- `rear()` returns `3`.
- After `clear()`, queue becomes `[]`.
- Final size is `0`.

## Note

`clear()` should leave the queue ready to be reused without creating a new instance.

## Required variables

- `queue`: queue with elements 1, 2, 3.
- `last_item`: result of `rear()` before clearing.
- `size_after_clear`: size after calling `clear()`.
