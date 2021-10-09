from functools import reduce


def plus_ten(x): return x + 10


print(plus_ten(1))

print(list(map(lambda x: x + 10, [1, 2, 3])))
print(list(map(lambda x: x ** 2, [1, 2, 3])))
print(list(map(str, [1, 2, 3])))

a = [i for i in range(1, 11)]
ex = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(ex)

a = [i for i in range(1, 6)]
b = [i for i in range(1, 11) if i % 2 == 0]
print(list(map(lambda x, y: x * y, a, b)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: x > 5 and x < 10, a)))

a = [i for i in range(1, 6)]
print(reduce(lambda x, y: x + y, a))
