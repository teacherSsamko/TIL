N, L, K = list(map(int, input().split()))
score = 0
easy, hard = 0, 0
for _ in range(N):
    sub1, sub2 = list(map(int, input().split()))
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

score += min(hard, K) * 140

if hard < K:
    score += min(K - hard, easy) * 100

print(score)
