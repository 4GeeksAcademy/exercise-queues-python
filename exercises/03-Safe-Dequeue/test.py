import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Queue, empty_queue, result_on_empty


def test_safe_dequeue():
    assert isinstance(empty_queue, Queue)
    assert result_on_empty is None
