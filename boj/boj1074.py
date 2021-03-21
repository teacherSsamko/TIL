def Z(N, x, y, r, c, answer=0):
    dx = [0, 1, -1, 2]
    dy = [0, 0, 1, 0]
    for i in range(4):
        x += dx[i]
        y += dy[i]
        if x == c and y == r:
            return answer
        answer += 1
    return Z(N, x, y, r, c, answer)


def solution(N, r, c):
    x, y = 0, 0
    n = 0
    cache = [(0, 0)] * (2**(N+1))
    dx = [0, 1, -1, 1]
    dy = [0, 0, 1, 0]
    # answer = Z(N, x, y, r, c, 0)
    answer = 0
    in_row = 2 ** (N-1)
    # print(in_row)
    for col in range(in_row):
        for row in range(in_row):
            x = 2 * row
            y = 2 * col
            for k in range(4):
                x += dx[k]
                y += dy[k]
                if x == c and y == r:
                    return answer
                answer += 1
    print((x, y))


N, r, c = list(map(int, input().split()))
print(solution(N, r, c))
