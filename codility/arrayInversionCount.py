def solution(A):
    if len(A) < 2:
        return 0

    ans = 0

    i = 0
    while i < len(A) and ans <= 1000000000:
        for curr in range(i + 1, len(A)):
            if A[i] > A[curr]:
                ans += 1
        i += 1

    if ans > 1000000000:
        return -1

    return ans
