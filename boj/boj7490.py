def solution(i, now, N, answer):
    global answers
    if i == N:
        if sum(now) == 0:
            answers.append(answer)
            return
        return
    else:
        i += 1
        solution(i, now+[i], N, answer + f'+{i}')
        solution(i, now+[-i], N, answer + f'-{i}')
        last_n = str(now[-1]) + f'{i}'
        last_n = int(last_n)
        solution(i, now[:-1]+[last_n], N, answer + f' {i}')


for i in range(int(input())):
    answers = []
    solution(1, [1], int(input()), '1')
    answers.sort()
    print("\n".join(answers))
    print()
