def compare_version(v1, v2):
    v1 = list(map(lambda x: int(x), v1.split(".")))
    v2 = list(map(lambda x: int(x), v2.split(".")))

    length = min(len(v1), len(v2))

    for i in range(length):
        v1_ = v1.pop(0)
        v2_ = v2.pop(0)
        if v1_ < v2_:
            return -1
        elif v1_ > v2_:
            return 1

    while v1:
        if v1.pop() > 0:
            return 1

    while v2:
        if v2.pop() > 0:
            return -1

    return 0


if __name__ == '__main__':
    v1, v2 = input().split()
    print(compare_version(v1, v2))
