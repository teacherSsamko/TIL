N, L, K = list(map(int, input().split()))
score = 0
quiz = {}
for _ in range(N):
    sub1, sub2 = list(map(int, input().split()))
    quiz[(sub1, sub2)] = 0

# quiz.sort(key=lambda x: x[1])
for q in quiz.keys():
    if q[1] <= L:
        quiz[q] = 140
    elif q[0] <= L:
        quiz[q] = 100

r_score = list(quiz.values())

r_score.sort(reverse=True)
for i in range(K):
    score += r_score[i]

print(score)
