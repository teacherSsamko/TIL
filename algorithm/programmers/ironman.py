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
    return bin(n).count("1")


n = 5000
print(solution(n))
