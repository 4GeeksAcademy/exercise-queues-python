## 08 - Priority Queue

## What you will learn

In this exercise you will process elements by priority.
The first output is not always the first input: the most urgent item goes first.

## What you need to implement

Create a simple priority queue where smaller number means higher priority.

Required methods:

- `enqueue(value, priority)`
- `dequeue()`
- `peek()`

If empty, `dequeue()` and `peek()` return `None`.

## Step-by-step guide

1. Store each element together with its priority.
2. In `enqueue`, insert each item in the correct position by priority.
3. In `dequeue`, remove the highest-priority item.
4. In `peek`, inspect the next item without removing it.
5. Create `pq` and enqueue:
   - ("low", 5)
   - ("urgent", 1)
   - ("normal", 3)
6. Run `dequeue()` three times and save results in `order`.

## Quick example

With those priorities, expected output order is:

1. `urgent`
2. `normal`
3. `low`

## Note

Higher priority means a smaller numeric value.

## Required variables

- `pq`: instance of `PriorityQueue`
- `order`: results of three `dequeue()` calls after enqueuing:
  - ("low", 5), ("urgent", 1), ("normal", 3)
