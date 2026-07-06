import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import PriorityQueue, order, pq


def test_priority_queue():
    assert isinstance(pq, PriorityQueue)
    assert order == ["urgent", "normal", "low"]
