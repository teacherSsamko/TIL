# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_ = {}
        for num in nums:
            if nums_.get(num):
                return num
            nums_[num] = True
