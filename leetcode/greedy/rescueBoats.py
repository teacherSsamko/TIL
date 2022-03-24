# https://leetcode.com/problems/boats-to-save-people/
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # greedy - two pointers
        ans = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1

        return ans
