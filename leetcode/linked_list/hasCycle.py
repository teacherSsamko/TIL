# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head

        link = {}
        while curr is not None:
            if link.get(curr):
                return True
            link[curr] = curr.next
            curr = curr.next

        return False
