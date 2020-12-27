buckets = []
p_cnt = 0


def pour(buckets, p_cnt):
    fr = buckets[p_cnt % 3][1]
    to = buckets[(p_cnt+1) % 3]
    if fr < to[0] - to[1]:
        amt = fr
    else:
        amt = to[0] - to[1]

    buckets[p_cnt % 3][1] -= amt
    buckets[(p_cnt+1) % 3][1] += amt

    return buckets


for i in range(3):
    c, m = list(map(int, input().split()))
    buckets.append([c, m])

while p_cnt < 100:
    buckets = pour(buckets, p_cnt)
    p_cnt += 1

for b in buckets:
    print(b[1])
