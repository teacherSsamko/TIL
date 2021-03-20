l = list()
for _ in range(int(input())):
    x, y = map(int, input().split())
    l.append((x, y))

result = sorted(l)
for r in result:
    print(r[0], r[1])
