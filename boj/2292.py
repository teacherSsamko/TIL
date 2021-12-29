r = int(input()) - 1
n = 1

if r == 0:
    print(1)
else:
    while True:
        if r > 0:
            n += 1
            r -= 6 * (n-1)
        else:
            print(n)
            break
