import random


def quick_sort(data):
    print(data)
    left, right = [], []
    if len(data) <= 1:
        return data
    pivot = data[0]
    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


sample = random.sample(range(100), 10)
print('end:', quick_sort(sample))


def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]
    return qsort(left) + [pivot] + qsort(right)


print(qsort(sample))
