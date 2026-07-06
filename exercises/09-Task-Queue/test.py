import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Task, TaskQueue, first_task_name, remaining_time, tasks


def test_task_queue():
    assert isinstance(tasks, TaskQueue)
    assert isinstance(Task("x", 1), Task)
    assert first_task_name == "setup"
    assert remaining_time == 18
