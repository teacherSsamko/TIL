def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n == 1:
        return n
    else:
        return False


def fact2(n):
    if n <= 1:
        return n
    return n * fact2(n - 1)


print(factorial(4))
print(fact2(4))
