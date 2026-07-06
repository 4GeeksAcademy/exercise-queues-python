import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import CircularQueue, cq, scenario


def test_circular_queue():
    assert isinstance(cq, CircularQueue)
    assert scenario == [True, True, True, False, 1, True, 2]
