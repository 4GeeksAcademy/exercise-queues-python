## 05 - Capacity Limit

## What you will learn

In this exercise you will control the maximum number of queue elements.
This is common when resources are limited, like memory or available slots.

## What you need to implement

Create a queue with a maximum capacity.

- Constructor: `Queue(capacity)`.
- `enqueue(value)`: returns `True` when inserted, `False` when full.
- `is_full()`: returns whether queue reached its capacity.

## Step-by-step guide

1. Store `capacity` in the constructor.
2. Create `self.items = []`.
3. In `is_full()`, compare `len(self.items)` with `capacity`.
4. In `enqueue()`, return `False` if full.
5. Otherwise append the value and return `True`.
6. Create `queue = Queue(2)`.
7. Try to enqueue 10, 20, and 30 and store results in `enqueue_results`.

## Quick example

With capacity 2:

- Enqueue 10 -> `True`
- Enqueue 20 -> `True`
- Enqueue 30 -> `False`

Expected result: `[True, True, False]`.

## Note

When an `enqueue` fails, the queue must keep its valid existing elements.

## Required variables

- `queue`: `Queue(2)`
- `enqueue_results`: list with enqueue results for 10, 20, 30.
