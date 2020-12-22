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

# 정확한 반복횟수 구하기
# 굳이 뒷 부분을 버리지 않아도 된다.
for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        result[j] += result[j+1]
    # print(result)

answer = "{}%".format(result[0] % 10*10 + result[1] % 10)
print(answer)
