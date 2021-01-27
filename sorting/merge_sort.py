import random


def merge_split(data):
    # print(data)
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    return merge(merge_split(left), merge_split(right))


def merge(left, right):
    data = []
    lp, rp = 0, 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            data.append(left[lp])
            lp += 1
        else:
            data.append(right[rp])
            rp += 1
    data += left[lp:]
    data += right[rp:]
    return data


sample = random.sample(range(100), 8)
print(merge_split(sample))
