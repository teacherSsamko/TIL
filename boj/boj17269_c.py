N, M = list(map(int, input().split()))
A, B = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(N, M)
for i in range(min_len):
    AB += A[i] + B[i]

# 남은 리스트 처리!
AB += A[min_len:] + B[min_len:]
# print(AB)

# 알파벳을 숫자로 치환!
result = [alp[ord(i) - ord('A')] for i in AB]

# print(result)

# 재귀 함수


def f(lst):
    tmp = []
    for i in range(len(lst) - 1):
        tmp.append((lst[i] + lst[i+1]) % 10)
    if len(tmp) == 2:
        return tmp
    else:
        return f(tmp)


result = f(result)

answer = "{}%".format(result[0] % 10*10 + result[1] % 10)
print(answer)
