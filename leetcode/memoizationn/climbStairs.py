# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i, n, memo):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = climb(i + 1, n, memo) + climb(i + 2, n, memo)
            return memo[i]

        memo = [0] * (n + 1)  # Memoization needs an initial array
        return climb(0, n, memo)
