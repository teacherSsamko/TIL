import sys


def merge_split(nl):
    if len(nl) <= 1:
        return nl
    mid = len(nl) // 2
    left = nl[:mid]
    right = nl[mid:]
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


nl = []
for _ in range(int(input())):
    nl.append(int(sys.stdin.readline()))

nl = merge_split(nl)
for n in nl:
    print(n)
