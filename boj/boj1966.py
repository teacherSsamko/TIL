def solution(N, M, Q):
    if N == 1:
        return 1
    queue = [(i, index) for index, i in enumerate(Q)]
    answer = 0
    # print(Q)
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            answer += 1
            if queue[0][1] == M:
                return answer
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


C = int(input())
for _ in range(C):
    N, M = list(map(int, input().split(" ")))
    Q = list(map(int, input().split(" ")))
    print(solution(N, M, Q))
