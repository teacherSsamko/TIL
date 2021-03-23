from collections import Counter


def solution(today):
    rank = [(-v, k) for k, v in Counter(today).items()]
    rank.sort()
    return rank[0][1]


today = []
for _ in range(int(input())):
    today.append(input())
print(solution(today))
