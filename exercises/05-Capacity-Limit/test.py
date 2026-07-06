import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Queue, enqueue_results, queue


def test_capacity_limit():
    assert isinstance(queue, Queue)
    assert enqueue_results == [True, True, False]
    assert queue.items == [10, 20]
