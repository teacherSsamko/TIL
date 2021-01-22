import random


def selection_sort(data):
    for std in range(len(data) - 1):
        min_index = std
        for idx in range(std + 1, len(data)):
            if data[idx] < data[min_index]:
                min_index = idx
        data[std], data[min_index] = data[min_index], data[std]
    return data


sample = random.sample(range(100), 50)
print(selection_sort(sample))
