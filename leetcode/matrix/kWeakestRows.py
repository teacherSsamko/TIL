# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = {sum(row): i for i, row in enumerate(mat)}

        power = [(sum(row), i) for i, row in enumerate(mat)]
        power.sort()

        weakest = [x[1] for x in power[:k]]

        return weakest
