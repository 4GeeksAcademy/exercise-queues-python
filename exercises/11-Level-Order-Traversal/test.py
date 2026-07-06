import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import TreeNode, level_order, root, traversal_result


def test_level_order_traversal():
    assert isinstance(root, TreeNode)
    assert callable(level_order)
    assert traversal_result == [1, 2, 3, 4, 5]
