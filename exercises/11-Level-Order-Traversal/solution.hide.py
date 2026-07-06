class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return result


root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3),
)
traversal_result = level_order(root)
