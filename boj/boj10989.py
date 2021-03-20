import sys


l = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    l[int(sys.stdin.readline())] += 1

for i in range(10001):
    if l[i]:
        for _ in range(l[i]):
            print(i)
