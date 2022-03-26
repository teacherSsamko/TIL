# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, target, left, right):
            if left < right and (right - left) > 1:
                pivot = (left + right) // 2
                if target == nums[pivot]:
                    return pivot
                elif target > nums[pivot]:
                    # find right
                    return binarySearch(nums, target, pivot, right)
                else:
                    return binarySearch(nums, target, left, pivot)
            else:
                if target == nums[left]:
                    return left
                elif target == nums[right]:
                    return right
                else:
                    return -1

        return binarySearch(nums, target, 0, len(nums) - 1)
