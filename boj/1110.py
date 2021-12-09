target = input()
if len(target) == 1:
    target = "0" + target

s_n = str(int(target[0]) + int(target[1]))
n = target[1] + s_n[-1]
cycle = 1

while n != target:
    s_n = str(int(n[0]) + int(n[1]))
    n = n[1] + s_n[-1]
    cycle += 1

print(cycle)
