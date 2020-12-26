N, M = list(map(int, input().split()))
groups = {}
for i in range(N):
    group_name = input()
    groups[group_name] = []
    n_group = int(input())
    for j in range(n_group):
        groups[group_name].append(input())

# print(groups)

for q in range(M):
    quiz, q_type = input(), int(input())
    if q_type:
        for k, v in groups.items():
            if quiz in v:
                print(k)
    else:
        print('\n'.join(sorted(groups[quiz])))
