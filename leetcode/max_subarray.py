# https://leetcode.com/problems/maximum-subarray/
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum
