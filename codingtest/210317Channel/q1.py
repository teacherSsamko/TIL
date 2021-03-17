def solution(b):
    from itertools import product
    from math import pow, sqrt
    al = [a for a in range(1, b+1)]
    for a in al:
        powC = pow(a, 2) + pow(b, 2)
        c = sqrt(powC)
        if c == int(c):
            # print(a, c)
            return int(c)
    return -1


bs = [4, 12, 5]
for b in bs:
    print(solution(b))
    # break

"""
answer 5 13 -1
"""
