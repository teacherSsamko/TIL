n = int(input())

count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
        continue
    x = str(i)
    if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]):
        count += 1

print(count)
