# buckets = []
C, M = list(), list()
p_cnt = 0


def pour(M, p_cnt):
    global C
    fr = M[p_cnt % 3]
    to = C[(p_cnt+1) % 3] - M[(p_cnt+1) % 3]
    if fr < to:
        amt = fr
    else:
        amt = to

    M[p_cnt % 3] -= amt
    M[(p_cnt+1) % 3] += amt

    return M


for i in range(3):
    c, m = list(map(int, input().split()))
    C.append(c)
    M.append(m)

while p_cnt < 100:
    idx = p_cnt % 3
    nxt = (p_cnt + 1) % 3
    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]),
                         0), min(C[nxt], M[nxt] + M[idx])
    p_cnt += 1

for b in M:
    print(b)
