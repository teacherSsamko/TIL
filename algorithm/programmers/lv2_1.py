"""
can Jump (passed tiles) * 2
can walk by 1 tile
jump doesn't consume battery
walk consume 1 battery

find lowest battery consume way and get how much battery needed

5 tiles 2 battery
6 tiles 2 battery
5000 tiles 5 battery
"""


def solution(n):
    ans = 0
    while n:
        if n % 2:
            ans += 1
        n = n // 2

    return ans


n = int(input())
print(solution(n))
