def solution(n, num_array):
    print(num_array)
    stack = []
    answer = []
    count = 1
    for i in range(1, n + 1):
        target = num_array[i]
        while target >= count:
            stack.append(count)
            answer.append("+")
            count += 1
        if stack[-1] == target:
            stack.pop()
            answer.append('-')
        else:
            print("NO")
            return
    print("\n".join(answer))
    return


n = int(input())
num_array = []
for _ in range(n):
    num_array.append(int(input()))

solution(n, num_array)
