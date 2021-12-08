h, m = list(map(int, input().split()))

# 45분 일찍

if m >= 45:
    m -= 45
elif m < 45 and h >= 1:
    h -= 1
    m += 15
else:
    h = 23
    m += 15
print("{0} {1}".format(h, m))
