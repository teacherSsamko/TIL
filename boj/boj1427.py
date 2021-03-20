N = input()
n_l = list(map(int, list(N)))
# n_l.sort(reverse=True)

# n_l = list(map(str, n_l))
# print("".join(n_l))

for i in range(9, -1, -1):
    for j in n_l:
        if i == int(j):
            print(j, end='')
