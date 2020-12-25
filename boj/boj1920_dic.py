N = int(input())
A = {i: 1 for i in input().split()}
M, B = int(input()), input().split()

for n in B:
    print(A.get(n, 0))
