def DFS(network, start):
    need_visit = list()
    visited = list()

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(network[node])

    return len(visited)


def solution(links):
    from collections import defaultdict
    network = defaultdict(list)
    for link in links:
        network[link[0]].append(link[1])
        network[link[1]].append(link[0])
        print(DFS(network, link[0]))

    return network


for _ in range(int(input())):
    links = []
    for x in range(int(input())):
        links.append(tuple(input().split(" ")))
    # print(links)
    network = solution(links)
    # print(network)
