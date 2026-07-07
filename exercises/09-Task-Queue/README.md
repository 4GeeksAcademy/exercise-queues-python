## 09 - Task Queue

## What you will learn

In this exercise you will model real tasks with a queue.
You will combine objects and FIFO behavior in one workflow.

## What you need to implement

Create:

- `Task(name, duration)` class to represent each task.
- `TaskQueue` class with:
	- `add_task(task)`
	- `next_task()`
	- `total_time()`

Rules:

- `next_task()` returns the next task in queue.
- If there are no tasks, `next_task()` returns `None`.
- `total_time()` sums pending task durations.

## Step-by-step guide

1. Define `Task` with name and duration.
2. In `TaskQueue`, store tasks in an internal list.
3. In `add_task`, append to the end.
4. In `next_task`, remove from the front.
5. In `total_time`, sum `duration` of all pending tasks.
6. Create `tasks` and add multiple tasks.
7. Save the first executed task name in `first_task_name`.
8. Save the pending total in `remaining_time`.

## Quick example

If you add tasks of 5, 3, and 2 minutes:

- The first one out should be the first one added.
- After executing one task, remaining time decreases by its duration.

## Note

In this challenge, order matters as much as the task data.

## Required variables

- `tasks`: instance of `TaskQueue`
- `first_task_name`: name of the first executed task
- `remaining_time`: total remaining time
