import heapq


def solution(nums, K):
    heapq.heapify(nums)
    result = None
    for _ in range(K):
        result = heapq.heappop(nums)
        # print(result)

    return result


N, K = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(nums, K))
