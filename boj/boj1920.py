def solution(N, M):
    N = {k: 1 for k in N}
    for m in M:
        print(N.get(m, 0))

    return


N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

solution(Ns, Ms)
