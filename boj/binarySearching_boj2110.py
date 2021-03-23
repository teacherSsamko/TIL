import sys


def solution(C, houses):
    answer = 0
    houses.sort()
    minGap = houses[1] - houses[0]
    maxGap = houses[-1] - houses[0]

    while minGap <= maxGap:
        midGap = (minGap + maxGap) // 2
        c = 1
        now_house = houses[0]
        for i in range(1, len(houses)):
            if houses[i] - now_house >= midGap:
                now_house = houses[i]
                c += 1
        if c >= C:
            minGap = midGap + 1
            answer = midGap
        else:
            maxGap = midGap - 1

    return answer


N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
print(solution(C, houses))
