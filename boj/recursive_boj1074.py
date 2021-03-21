def solution(sz, x, y):
    if sz == 1:
        return 0

    sz //= 2
    for row in range(2):
        for col in range(2):
            if x < sz * (col + 1) and y < sz * (row + 1):
                return (row*2+col) * sz*sz + solution(sz, x-sz*col, y-sz*row)


result = 0
N, r, c = map(int, input().split())
# 1 3
print(solution(2 ** N, c, r))
