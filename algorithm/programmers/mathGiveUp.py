def solution(answers):
    rank = []
    multiple = len(answers) // 40 + 1
    p1_ans = [1, 2, 3, 4, 5] * 8  # 5
    p2_ans = [2, 1, 2, 3, 2, 4, 2, 5] * 5  # 8
    p3_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4  # 10
    print(multiple)
    ps_answers = [p1_ans, p2_ans, p3_ans]
    ps_answers = [x * multiple for x in ps_answers]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            if ps_answers[j][i] == answers[i]:
                scores[j] += 1
    print(scores)
    top_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == top_score:
            rank.append(i + 1)

    return rank


answers = [1, 3, 2, 4, 2, 2, 5, 1, 2, 4, 1, 4, 2, 5, 1, 2, 3] * 30
print(solution(answers))
