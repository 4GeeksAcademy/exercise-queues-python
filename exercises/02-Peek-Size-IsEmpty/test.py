import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Queue, front_item, queue, queue_length


def test_peek_size_is_empty():
    assert isinstance(queue, Queue)
    assert front_item == "A"
    assert queue_length == 3
    assert queue.is_empty() is False
