def find(x, parents):
    if parents[x] == x:
        return x
    p = find(parents[x], parents)
    parents[x] = p
    return parents[x]


def union(x, y, parents, network_size):
    x = find(x, parents)
    y = find(y, parents)

    if x != y:
        parents[y] = x
        network_size[x] += network_size[y]
    # print(parents)


def solution(links):
    parents = dict()
    network_size = dict()
    for link in links:
        x, y = link
        if x not in parents:
            parents[x] = x
            network_size[x] = 1
        if y not in parents:
            parents[y] = y
            network_size[y] = 1
        union(x, y, parents, network_size)
        print(network_size[find(x, parents)])


for _ in range(int(input())):
    links = []
    for x in range(int(input())):
        links.append(list(input().split(" ")))
    # print(links)
    network = solution(links)
    # print(network)
