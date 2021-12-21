case_n = int(input())

for _ in range(case_n):
    r, s = input().split()
    s = list(s)
    s = list(map(lambda x: x * int(r), s))
    print(''.join(s))
