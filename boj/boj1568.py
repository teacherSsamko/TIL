def solution(N):
    i = 1
    answer = 0
    while N > 0:
        if N - i >= 0:
            N -= i
            i += 1
        else:
            i = 1
            continue
        answer += 1

    return answer


print(solution(int(input())))
