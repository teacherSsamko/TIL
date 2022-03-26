# https://leetcode.com/problems/invert-binary-tree/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: TreeNode):
            node.left, node.right = node.right, node.left

            return node

        queue = deque()
        curr = root

        while queue or curr:
            if curr:
                curr = invert(curr)
                queue.append(curr.left)
                queue.append(curr.right)

            curr = queue.popleft()

        return root
