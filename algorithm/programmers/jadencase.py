def solution(s):
    tmp = s.split(" ")
    answer = ''
    for w in tmp:
        answer += w.capitalize() + " "
    return answer[:-1]


s = input()
print(solution(s))
