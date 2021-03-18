def solution(n, weak, dist):
    def get_dist(n1, n2):
        return min(abs(n1 - n2), n1 + 12 - n2)
    import heapq
    answer = 0
    friends_n = len(dist)
    to_check = len(weak)
    checked = 0
    edges = []
    for i in range(to_check):
        if i == to_check - 1:
            edges.append((get_dist(weak[0], weak[i]), weak[0], weak[i]))
        else:
            edges.append((get_dist(weak[i], weak[i+1]), weak[i], weak[i + 1]))
    print(edges)

    heapq.heapify(edges)
    print(edges)
    while checked < to_check:
        edge = heapq.heappop(edges)
        length = edge[0]
        for i in range(len(dist)):
            if dist[i] > length:
                answer += 1
                checked += 2
                break
        del dist[i]

    print(dist)

    return answer


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
ans = 1
print(solution(n, weak, dist))
