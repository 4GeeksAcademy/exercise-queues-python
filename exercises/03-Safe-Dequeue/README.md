## 03 - Safe Dequeue

## What you will learn

In this exercise you will make your queue more robust.
The goal is to handle empty cases safely.

## What you need to implement

Modify `dequeue()` so it:

- Removes and returns the front when elements exist.
- Returns `None` when the queue is empty.

## Step-by-step guide

1. In `dequeue()`, check first if the queue is empty.
2. If it is empty, return `None`.
3. If it has elements, use `pop(0)` to remove and return the front.
4. Create an empty queue in `empty_queue`.
5. Save the result of `empty_queue.dequeue()` in `result_on_empty`.

## Quick example

- Empty queue: `dequeue()` returns `None`.
- Queue with `[7, 8]`: `dequeue()` returns `7` and queue becomes `[8]`.

## Note

Handling empty cases prevents runtime failures.

## Required variables

- `empty_queue`: empty queue.
- `result_on_empty`: result of `dequeue()` on an empty queue.
