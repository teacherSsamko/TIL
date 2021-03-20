l = list()
for _ in range(int(input())):
    l.append(int(input()))


def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]
    return qsort(left) + [pivot] + qsort(right)


result = qsort(l)
for r in result:
    print(r)
