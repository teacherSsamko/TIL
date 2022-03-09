# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, values: list):
        self.head = ListNode(values.pop(0))
        cur = self.head
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next


class Solution:
    @classmethod
    def result(cls, head: Optional[ListNode]):
        ssl_head = cls.deleteDuplicate(head)
        result_list = []
        while ssl_head:
            result_list.append(ssl_head.val)
            ssl_head = ssl_head.next

        return result_list

    @staticmethod
    def deleteDuplicate(head: Optional[ListNode]):
        sentinel = ListNode(0, head)

        pred = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next

        return sentinel.next


if __name__ == "__main__":
    test1 = [1, 2, 3, 3, 4, 4, 5]
    testList = SinglyLinkedList(test1)
    print(Solution.result(testList.head))
    test2 = [1, 1, 1, 2, 3]
    testList = SinglyLinkedList(test2)
    print(Solution.result(testList.head))
