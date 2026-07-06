import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import Queue, last_item, queue, size_after_clear


def test_rear_and_clear():
    assert isinstance(queue, Queue)
    assert last_item == 3
    assert size_after_clear == 0
