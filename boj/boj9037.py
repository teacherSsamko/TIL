T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    # 처음 홀수개 사탕 짝수개로 만들기
    for i in range(N):
        if C[i] % 2 != 0:
            C[i] += 1
    result = 0
    while True:
        if min(C) == max(C):
            break
        half = [x // 2 for x in C]
        C = half.copy()
        half = half[1:] + half[:1]
        C = list(map(lambda x, y: x + y, C, half))
        for i in range(N):
            if C[i] % 2 != 0:
                C[i] += 1
        result += 1
    print(result)
