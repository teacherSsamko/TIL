import random


def multiple(num):
    return_value = 1
    for i in range(1, num + 1):
        return_value = return_value * i
    return return_value


def multiple_re(n):
    if n <= 1:
        return n
    return n * multiple_re(n - 1)


print(multiple_re(4))

data = random.sample(range(10), 3)


def sum_list(data):
    if len(data) == 1:
        return data.pop()
    return data.pop() + sum_list(data)


print(data)
print(sum_list(data))


def isPalindrome(word):
    if len(word) == 1:
        return True
    for i in range(len(word) // 2):
        if word[i] == word[-i - 1]:
            continue
        else:
            return False
    return True


def isPalindrome_re(word):
    if len(word) == 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome_re(word[1:-1])


print(isPalindrome("laefvfeal"))
print(isPalindrome("motor"))

print(isPalindrome_re("laefvfeal"))
print(isPalindrome_re("motor"))
