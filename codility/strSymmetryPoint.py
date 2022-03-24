def solution(S):
    length = len(S)
    if length == 0:
        return -1

    if length <= 1:
        return 0

    if length % 2 == 0:
        return -1

    reverse = list(reversed(S))

    return length // 2 if S == "".join(reverse) else -1
