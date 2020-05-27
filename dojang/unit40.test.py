def prime_number_generator(start, stop):
    for i in range(start, stop + 1):
        isPrime = True

        for x in range(2, i):
            if i % x == 0:
                isPrime = False
                break
        if isPrime:
            yield i


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
