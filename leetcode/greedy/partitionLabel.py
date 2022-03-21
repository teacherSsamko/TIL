from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {c: i for i, c in enumerate(s)}
        # anchor & j are the key.
        j = anchor = 0
        ans = []

        for i, c in enumerate(s):
            j = max(j, last_pos[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans
