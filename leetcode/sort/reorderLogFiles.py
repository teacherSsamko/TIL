# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # divide logs into two groups of letter and digit
        letters = []
        digits = []
        for log in logs:
            _id, rest = log.split(" ", maxsplit=1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # order letters
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return rest, _id
        letters.sort(key=get_key)

        # merge two groups
        return letters + digits
