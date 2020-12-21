"""
list.append() 보다
list[i]로 값을 update하는 것이 빠르다.
"""

n, lst = int(input()), list(map(int, input().split()))

result = [0 for i in range(n)]
result[0] = lst[0]

for i in range(1, n):
    tmp = (lst[i] * (i+1)) - sum(result)
    # result.append(tmp)
    result[i] = tmp

result = list(map(str, result))
print(' '.join(result))
