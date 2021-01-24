# fibonacci

# use recursive call
def fibo(n):
    print('recursive', n)
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(4))

# use DP


def fibo_dp(n):
    cache = [0 for i in range(n + 1)]
    cache[0] = 0
    cache[1] = 1

    print('dp', cache)
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
        print('dp', cache)

    return cache[n]


print(fibo_dp(4))
