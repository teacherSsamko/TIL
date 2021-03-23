def solution(trophies):
    left = []

    for i in range(len(trophies)):
        if i == 0:
            left.append(trophies[0])
            continue
        if left[-1] < trophies[i]:
            left.append(trophies[i])

    right = []
    trophies = list(reversed(trophies))

    for i in range(len(trophies)):
        if i == 0:
            right.append(trophies[0])
            continue
        if right[-1] < trophies[i]:
            right.append(trophies[i])

    print(len(left))
    print(len(right))

    return


trophies = []
for _ in range(int(input())):
    trophies.append(int(input()))
solution(trophies)
