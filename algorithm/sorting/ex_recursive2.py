def ex(n):
    print(n)
    if n == 1:
        return True
    elif n % 2 != 0:
        return ex(3 * n + 1)
    else:
        return ex(n // 2)


ex(3)


def ex2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return ex2(n - 1) + ex2(n - 2) + ex2(n - 3)


print(ex2(5))
