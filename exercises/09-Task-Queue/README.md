## 09 - Task Queue

Create a task queue using a `Task` class.

- `Task(name, duration)`
- `TaskQueue.add_task(task)`
- `TaskQueue.next_task()`
- `TaskQueue.total_time()` sums pending durations.

`next_task()` returns `None` if there are no tasks.

## Required variables

- `tasks`: instance of `TaskQueue`
- `first_task_name`: name of the first executed task
- `remaining_time`: total remaining time
