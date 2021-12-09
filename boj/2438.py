n = int(input())

for i in range(n):
    s = "*"
    a = " "
    print(a * (n - i - 1), end="")
    print(s * (i + 1))
