
def find(z, parent):
    if z == parent[z]:
        return z
    else:
        p = find(parent[z], parent)
        parent[z] = p
        return parent[z]


def union(x, y, parent, size):
    print(parent)
    x = find(x, parent)
    y = find(y, parent)

    if x != y:
        parent[y] = x
        size[x] += size[y]


def solution(links):
    parent = dict()
    size = dict()
    for link in links:
        x, y = link
        if not parent.get(x):
            parent[x] = x
            size[x] = 1
        if not parent.get(y):
            parent[y] = y
            size[y] = 1
        union(x, y, parent, size)

        print(size[find(x, parent)])


for _ in range(int(input())):
    links = []
    for x in range(int(input())):
        links.append(list(input().split(" ")))
    # print(links)
    network = solution(links)
    # print(network)
