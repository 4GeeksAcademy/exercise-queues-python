## 01 - Queue Basics

## What you will learn

In this exercise you will build your first queue in Python.
A queue follows FIFO: first in, first out.

Think of a line of people:

- A new person joins at the end.
- The person who leaves is the one at the front.

## What you need to implement

Create a `Queue` class with an internal list (`self.items`) and these methods:

- `enqueue(value)`: add a value to the end of the queue.
- `dequeue()`: remove and return the value at the front.

## Step-by-step guide

1. In `__init__`, create `self.items = []`.
2. In `enqueue`, use `append` to insert at the end.
3. In `dequeue`, use `pop(0)` to remove the first element.
4. Create an instance named `queue`.
5. Enqueue `10` and `20`.
6. Save the result of the first `dequeue()` into `first_out`.

## Quick example

If you do:

1. `enqueue(10)`
2. `enqueue(20)`
3. `dequeue()`

Then:

- The returned value must be `10`.
- The queue must end as `[20]`.

## Note: imports

You do not need imports to solve the queue logic in this exercise.
A `Queue` class and an internal list (`self.items`) are enough to complete the challenge.

## Required variables

- `queue`: instance of `Queue`.
- You must enqueue `10` and `20`.
- `first_out`: result of the first `dequeue()`.
