def solution(logs):
    cursor = 0
    origin = []
    buffer = []
    for log in logs:
        if log == "<":
            if origin:
                buffer.append(origin.pop())
        elif log == ">":
            if buffer:
                origin.append(buffer.pop())
        elif log == "-":
            if origin:
                origin.pop()
        else:
            origin.append(log)

    return "".join(origin + buffer[::-1])


N = int(input())
for _ in range(N):
    print(solution(input()))
