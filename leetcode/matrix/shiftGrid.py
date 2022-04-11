# https://leetcode.com/problems/shift-2d-grid/submissions/
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for _ in range(k):
            new_grid = [[0] * n for _ in range(m)]

            # Case 1: Move everything not in the last column
            for row in range(m):
                for col in range(n - 1):
                    new_grid[row][col + 1] = grid[row][col]

            # Case 2: Move last column, but no last row
            for row in range(m - 1):
                new_grid[row + 1][0] = grid[row][n - 1]

            # Case 3: Bottom right item
            new_grid[0][0] = grid[m - 1][n - 1]

            grid = new_grid

        return grid
