## 07 - Queue With Two Stacks

## What you will learn

In this exercise you will implement a queue using two stacks.
You will combine structures to reproduce FIFO behavior.

## What you need to implement

Implement a `QueueWithStacks` class using:

- `in_stack` for `enqueue`.
- `out_stack` for `dequeue` and `peek`.

Required methods:

- `enqueue(value)`
- `dequeue()`
- `peek()`

If empty, `dequeue()` and `peek()` must return `None`.

## Step-by-step guide

1. In `enqueue`, append to `in_stack`.
2. When you need front access and `out_stack` is empty, move elements from `in_stack` to `out_stack` one by one.
3. In `dequeue`, return `out_stack.pop()`.
4. In `peek`, return `out_stack[-1]`.
5. If both stacks are empty, return `None`.
6. Run the required sequence and save outputs in `results`.

## Quick example

Sequence:

1. enqueue(5)
2. enqueue(6)
3. dequeue()
4. peek()
5. dequeue()
6. dequeue()

You should see FIFO order and finally `None` when queue is empty.

## Note

Moving data from `in_stack` to `out_stack` reverses order and enables front removal.

## Required variables

- `queue`: instance of `QueueWithStacks`
- `results`: results of:
  - enqueue(5), enqueue(6), dequeue(), peek(), dequeue(), dequeue()
