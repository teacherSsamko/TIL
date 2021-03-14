def solution(num, k):

    stack = list()
    for n in num:
        print(stack)
        while stack and k and stack[-1] < n:
            k -= 1
            stack.pop()
        stack.append(n)
    if k != 0:
        print('here', k)
        stack = stack[:-k]

    return "".join(stack)


if __name__ == '__main__':
    num, k = input().split()
    print(solution(num, int(k)))
