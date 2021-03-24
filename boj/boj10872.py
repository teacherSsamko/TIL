def fact(N):
    cache = [1] * (N+1)

    for i in range(2, N + 1):
        cache[i] = cache[i-1] * i

    return cache[N]


print(fact(int(input())))
