from math import ceil

day, night, target = map(int, input().split())

target -= day
n = 1

n += ceil(target / (day - night))
print(n)
