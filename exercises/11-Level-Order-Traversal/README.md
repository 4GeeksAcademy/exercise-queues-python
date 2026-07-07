## 11 - Level Order Traversal

## What you will learn

In this exercise you will use a queue to traverse a binary tree level by level.
This traversal is also known as BFS.

## What you need to implement

Implement:

- `TreeNode(value, left=None, right=None)` class.
- `level_order(root)` function that returns BFS traversal as a list.

If the tree is empty, return an empty list.

## Step-by-step guide

1. If `root` is `None`, return `[]`.
2. Create a queue and enqueue `root`.
3. Create a results list.
4. While queue is not empty:
   - dequeue front node.
   - append its value to results.
   - enqueue left child if it exists.
   - enqueue right child if it exists.
5. Return the final results list.
6. Build the required tree and save output in `traversal_result`.

## Quick example

For this tree:

- root 1
- children of 1: 2 and 3
- children of 2: 4 and 5

Expected level-order result: `[1, 2, 3, 4, 5]`.

## Note

The queue ensures all nodes in one level are processed before moving to the next.

## Required variables

- `root`: tree with structure:
  - 1
  - children: 2 and 3
  - children of 2: 4 and 5
- `traversal_result`: result of `level_order(root)`
