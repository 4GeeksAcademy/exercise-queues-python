## 06 - Circular Queue

## What you will learn

In this exercise you will build a fixed-size circular queue.
The key idea is reusing freed positions after the front moves.

## What you need to implement

Implement a `CircularQueue` class with fixed capacity and methods:

- `enqueue(value)`
- `dequeue()`
- `peek()`
- `is_empty()`
- `is_full()`

Rules:

- If `enqueue` fails because queue is full, return `False`.
- If `dequeue` fails because queue is empty, return `None`.

## Step-by-step guide

1. Create a fixed-size array for storage.
2. Track front and rear indexes.
3. Track current count to detect empty/full quickly.
4. In `enqueue`, insert at rear and move rear circularly.
5. In `dequeue`, remove from front and move front circularly.
6. In `peek`, return front value without removing it.
7. Run the required sequence and save outputs in `scenario`.

## Quick example

With `CircularQueue(3)` and this sequence:

1. enqueue(1)
2. enqueue(2)
3. enqueue(3)
4. enqueue(4)
5. dequeue()
6. enqueue(4)
7. peek()

The 4th enqueue should fail first, then after `dequeue()` frees space, the next enqueue should succeed.

## Note

In a circular queue, indexes wrap back to the start when they reach the end.

## Required variables

- `cq`: `CircularQueue(3)`
- `scenario`: list of results from this sequence:
  - enqueue(1), enqueue(2), enqueue(3), enqueue(4), dequeue(), enqueue(4), peek()
