# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getLongest(node: TreeNode):
            if node is None:
                return 0
            nonlocal diameter

            left_path = getLongest(node.left)
            right_path = getLongest(node.right)

            diameter = max(left_path + right_path, diameter)

            return max(left_path, right_path) + 1

        getLongest(root)

        return diameter
