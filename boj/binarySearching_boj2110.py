import sys
from itertools import combinations


def solution(C, houses):
    answer = 0
    houses.sort()
    tmp_l = [houses.pop(0), houses.pop()]
    ps = combinations(houses, C-2)
    min_dists = []
    for p in ps:
        p = tmp_l[:1] + list(p) + tmp_l[1:]
        mind = p[-1]
        for i in range(len(p) - 1):
            if p[i + 1] - p[i] < mind:
                mind = p[i + 1] - p[i]
        min_dists.append(mind)

    return max(min_dists)


N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
print(solution(C, houses))
