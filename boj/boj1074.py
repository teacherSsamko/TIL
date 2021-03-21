def solution(n, x, y):
    global result
    if n == 2:
        if x == c and y == r:
            print(result)
            return
        result += 1
        if x + 1 == c and y == r:
            print(result)
            return
        result += 1
        if x == c and y + 1 == r:
            print(result)
            return
        result += 1
        if x + 1 == c and y + 1 == r:
            print(result)
            return
        result += 1
        return
    solution(n / 2, x, y)
    solution(n / 2, x + n // 2, y)
    solution(n / 2, x, y + n//2)
    solution(n / 2, x + n//2, y + n//2)


result = 0
N, r, c = map(int, input().split())
solution(2 ** N, 0, 0)
