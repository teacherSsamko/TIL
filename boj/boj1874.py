def solution(n, num_array):
    print(num_array)
    ns = [x for x in range(1, n+1)]
    print(ns)
    stack = [ns.pop(0)]
    goal = []
    answer = ['+']
    cursor = 0
    while goal != num_array:
        if stack and stack[-1] == num_array[cursor]:
            goal.append(stack.pop())
            answer.append('-')
            cursor += 1
        elif ns:
            stack.append(ns.pop(0))
            answer.append('+')
        else:
            answer = ["NO"]
            break
    print(goal)
    print(stack)
    for ans in answer:
        print(ans)
    return


n = int(input())
num_array = []
for _ in range(n):
    num_array.append(int(input()))

solution(n, num_array)
