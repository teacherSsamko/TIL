import math
import heapq


def solution(nums):
    exists = {}

    for i, num in enumerate(nums):
        if exists.get(num) != None:
            exists[num] = math.inf
        else:
            exists[num] = i

    heap = []
    for num in exists.keys():
        heapq.heappush(heap, (exists[num], num))

    return heap[0][1] if heap[0][0] < math.inf else -1

    # Edge Case: [1, 1, 1, 2, 3, 3, 3]
