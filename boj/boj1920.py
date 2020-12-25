N = int(input())
A = set(input().split())
M, B = int(input()), input().split()

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
