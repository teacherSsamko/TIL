def solution(logs):
    cursor = 0
    origin = []
    for log in logs:
        if log == "<":
            if cursor > 0:
                cursor -= 1
        elif log == ">":
            if cursor < len(origin):
                cursor += 1
        elif log == "-":
            if origin and cursor > 0:
                del origin[cursor - 1]
                cursor -= 1
        else:
            origin.insert(cursor, log)
            cursor += 1

    return "".join(origin)


N = int(input())
for _ in range(N):
    print(solution(input()))
