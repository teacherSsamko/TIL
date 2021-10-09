def countdown(n):
    n = n + 1

    def count():
        nonlocal n
        n -= 1
        return n
    return count


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')
