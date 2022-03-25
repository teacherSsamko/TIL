# Greedy - medium
# https://leetcode.com/problems/two-city-scheduling/
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        costs.sort(key=lambda x: x[0] - x[1])

        return sum([x[0] for x in costs[:n]]) + sum([x[1] for x in costs[n:]])
