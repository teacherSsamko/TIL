import random


def binary_search(value, data):
    print(data)
    if len(data) == 1:
        if value == data[0]:
            return True
        else:
            return False

    i = len(data) // 2
    if value == data[i]:
        return True
    elif value < data[i]:
        return binary_search(value, data[:i])
    elif value > data[i]:
        return binary_search(value, data[i:])


sample = random.sample(range(70), 10)
sample.sort()
print(sample)
print(binary_search(41, sample))
