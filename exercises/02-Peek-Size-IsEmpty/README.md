## 02 - Peek, Size and Is Empty

## What you will learn

In this exercise you will add query methods to a queue.
These methods let you inspect information without changing queue contents.

## What you need to implement

Extend the `Queue` class with:

- `peek()`: returns the front element without removing it.
- `size()`: returns the current number of elements.
- `is_empty()`: returns `True` when the queue is empty, otherwise `False`.

## Step-by-step guide

1. Keep `self.items` as the internal list.
2. In `peek()`, return `self.items[0]` when there are elements.
3. If there are no elements in `peek()`, return `None`.
4. In `size()`, return `len(self.items)`.
5. In `is_empty()`, check if the size is zero.
6. Create `queue`, enqueue "A", "B", "C" and save:
	- `front_item = queue.peek()`
	- `queue_length = queue.size()`

## Quick example

If the queue contains `['A', 'B', 'C']`:

- `peek()` should return `A`.
- `size()` should return `3`.
- `is_empty()` should return `False`.

## Note

`peek()` must not remove elements. It only looks at the front.

## Required variables

- `queue`: instance of `Queue`.
- Enqueue "A", "B", "C".
- `front_item`: result of `peek()`.
- `queue_length`: result of `size()`.
