def dfs(array, numbers, target, size):
    answer = 0
    if len(array) == size:
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(array + [numbers[0]], numbers[1:], target, size)
        answer += dfs(array + [-numbers[0]], numbers[1:], target, size)
    return answer


def solution(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
