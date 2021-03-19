scores = list(map(int, input().split()))


def solution(scores):
    asc = True
    desc = True
    for i in range(len(scores) - 1):
        if scores[i + 1] - scores[i] > 0:
            desc = False
        else:
            asc = False

    if asc:
        return "ascending"
    elif desc:
        return "descending"
    else:
        return "mixed"


print(solution(scores))
