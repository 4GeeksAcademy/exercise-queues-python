import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import QueueWithStacks, queue, results


def test_queue_with_two_stacks():
    assert isinstance(queue, QueueWithStacks)
    assert results == [True, True, 5, 6, 6, None]
