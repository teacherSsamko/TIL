def solution(numbers):
    def check_prime(n):
        from math import sqrt
        k = int(sqrt(n)) + 1
        if n < 2:
            return False

        for i in range(2, k):
            if n % i == 0:
                return False
        return True

    from itertools import permutations
    answer = []
    numbers = list(numbers)
    num_set = set()
    for i in range(1, len(numbers) + 1):
        numbersP = permutations(numbers, i)
        for num in numbersP:
            n = "".join(list(num))
            num_set.add(int(n))
    num_l = list(num_set)
    for n in num_l:
        if check_prime(n):
            answer.append(n)

    return len(set(answer))


numbers = input()
print(solution(numbers))
