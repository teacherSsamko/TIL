# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals: set, anti_diagonals: set, cols: set):
            if row == n:
                return 1

            ans = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_antidiagonal = row + col

                if (col in cols or curr_diagonal in diagonals or curr_antidiagonal in anti_diagonals):
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_antidiagonal)

                ans += backtrack(row + 1, diagonals, anti_diagonals, cols)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_antidiagonal)

            return ans

        return backtrack(0, set(), set(), set())
