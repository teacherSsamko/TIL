import random


class Bubble:
    def __init__(self, array=None):
        if not array:
            self.array = [5, 2, 3, 1]

    def swap(self, f, b):
        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        self.isSwapped = True

    def sort(self):
        self.isSwapped = False
        turn = len(self.array) - 1
        for i in range(turn):
            for j in range(turn - i):  # turn - i 가 중요.
                if self.array[j] > self.array[j + 1]:
                    self.swap(self.array[j], self.array[j + 1])
            print(self.array)


def bubblesort(data):
    n = 0
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j+1], data[j]
                swap = True
            n += 1
        if not swap:
            break
    print(n)
    return data


data_list = random.sample(range(100), 50)
print(data_list)
print(bubblesort(data_list))
