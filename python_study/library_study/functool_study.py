from itertools import product

l = [(1, -1), (2, 3), (5, -5)]
print(product(*l))
for x in product(*l):
    print(x)
s = list(map(sum, product(*l)))
print(s)

bi = product(range(2), repeat=3)
for x in bi:
    print(x)
