N, M = list(map(int, input().split()))
groups_mem, mem_groups = {}, {}
for i in range(N):
    group_name = input()
    groups_mem[group_name] = []
    n_group = int(input())
    for j in range(n_group):
        _name = input()
        groups_mem[group_name].append(_name)
        mem_groups[_name] = group_name


# print(groups)

for q in range(M):
    quiz, q_type = input(), int(input())
    if q_type:
        print(mem_groups[quiz])
    else:
        print('\n'.join(sorted(groups_mem[quiz])))
