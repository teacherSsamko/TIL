def check(candy):
    return len(set(candy)) == 1


def teacher(N, candy):
    for i in range(N):
        if candy[i] % 2 != 0:
            candy[i] += 1
    candy = [x // 2 for x in candy]
    half = candy[1:] + candy[:1]
    candy = list(map(lambda x, y: x + y, candy, half))
    return candy


def process():
    N, candy = int(input()), list(map(int, input().split()))
    candy = teacher(N, candy)
    cnt = 0
    while not check(candy):
        cnt += 1
        candy = teacher(N, candy)
    return cnt


T = int(input())
for _ in range(T):
    print(process())
