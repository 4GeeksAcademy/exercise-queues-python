import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Queue, first_out, queue


def test_queue_basics():
    assert isinstance(queue, Queue)
    assert first_out == 10
    assert queue.items == [20]
