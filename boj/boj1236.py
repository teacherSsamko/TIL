def solution(N, M, castle):
    rows = [0] * N
    cols = [0] * M
    for i in range(N):
        for j in range(M):
            if castle[i][j] == 'X':
                rows[i] = 1
                cols[j] = 1

    return max(rows.count(0), cols.count(0))


N, M = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(list(input()))
print(solution(N, M, castle))
