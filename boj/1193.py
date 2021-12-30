x = int(input())

if x == 1:
    print("1/1")
    exit()

for n in range(x):
    if n * (n + 1) // 2 <= x and x < (n + 1) * (n + 2) // 2:
        total = n + 2
        rest = x - (n * (n + 1) // 2)
        break

if rest:
    if total % 2 == 0:
        parent = rest
        son = total - parent
    else:
        son = rest
        parent = total - son
else:
    if total % 2 == 0:
        parent = rest + 1
        son = total - parent - 1
    else:
        son = rest + 1
        parent = total - son - 1

print(f"{son}/{parent}")
