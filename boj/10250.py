T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    # YYXX, YXX
    Y = N % H
    X = N // H + 1
    if N % H == 0:
        Y = H
        X -= 1
    print(f"{Y}{X:02}")
