class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ""

        for i in range(n):
            positionLeft = n - i - 1
            if k > positionLeft * 26:
                add = k - (positionLeft * 26)
                ans += chr(add + 96)
                k -= add
            else:
                ans += "a"
                k -= 1

        return ans
