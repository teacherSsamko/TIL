import random


def insertion_sort(data):
    for std in range(1, len(data) - 1):
        for idx in range(std + 1, 0, -1):
            if data[idx] < data[idx - 1]:
                data[idx], data[idx - 1] = data[idx - 1], data[idx]
            else:
                break
    return data


sample = random.sample(range(100), 50)
print(insertion_sort(sample))
