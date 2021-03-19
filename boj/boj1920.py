def solution(N, M):
    N = {k: 1 for k in N}
    for m in M:
        if N.get(m):
            print(1)
        else:
            print(0)

    return


N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

solution(Ns, Ms)
