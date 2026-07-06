## 06 - Circular Queue

Implement a circular queue with a fixed-size array.

Required methods:

- `enqueue(value)`
- `dequeue()`
- `peek()`
- `is_empty()`
- `is_full()`

If enqueue fails because the queue is full, return `False`.
If dequeue fails because the queue is empty, return `None`.

## Required variables

- `cq`: `CircularQueue(3)`
- `scenario`: list of results from this sequence:
  - enqueue(1), enqueue(2), enqueue(3), enqueue(4), dequeue(), enqueue(4), peek()
