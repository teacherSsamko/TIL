import random


def sequential_search(value, data):
    for i in range(len(data)):
        if value == data[i]:
            return i
    return False


sample = random.sample(range(30), 10)
print(sample)
print(sequential_search(10, sample))
