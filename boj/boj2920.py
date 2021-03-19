scores = list(map(int, input().split()))


def solution(scores):
    asc = 0
    desc = 0
    now = scores.pop(0)
    for nxt in scores:
        if nxt - now > 0:
            asc += 1
        else:
            desc += 1
        now = nxt
    if asc and desc:
        return "mixed"
    if asc:
        return "ascending"
    else:
        return "descending"


print(solution(scores))
