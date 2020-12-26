N, L, K = list(map(int, input().split()))
score = 0
quiz = []
for _ in range(N):
    sub1, sub2 = list(map(int, input().split()))
    quiz.append((sub1, sub2))

quiz.sort(key=lambda x: x[1])


for i in range(K):
    sub1, sub2 = quiz[i]
    if sub2 <= L:
        score += 140
    elif sub1 <= L:
        score += 100
    else:
        continue
print(score)
