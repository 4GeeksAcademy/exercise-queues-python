import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import hot_potato, winner


def test_hot_potato():
    assert callable(hot_potato)
    assert winner == "Ana"
