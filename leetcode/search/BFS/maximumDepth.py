# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        ans = depth = 0

        while stack:
            depth, root = stack.pop()
            if root:
                ans = max(ans, depth)
                stack.append((depth + 1, root.left))
                stack.append((depth + 1, root.right))

        return ans
