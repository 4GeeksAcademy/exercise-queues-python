from dataclasses import dataclass


@dataclass
class Task:
    name: str
    duration: int


class TaskQueue:
    def __init__(self):
        self.items = []

    def add_task(self, task):
        self.items.append(task)

    def next_task(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def total_time(self):
        return sum(task.duration for task in self.items)


tasks = TaskQueue()
tasks.add_task(Task("setup", 5))
tasks.add_task(Task("build", 10))
tasks.add_task(Task("deploy", 8))
first_task = tasks.next_task()
first_task_name = first_task.name if first_task else None
remaining_time = tasks.total_time()
