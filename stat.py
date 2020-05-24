import math

d = [1, 2, 3, 4, 5]
print(d)

mean = sum(d) / len(d)
print("mean =", mean)

vsum = 0
for x in d:
    vsum = vsum + (x - mean)**2
var = vsum / len(d)
print(var)

std = math.sqrt(var)
std = format(std, ".2f")
print(std)
