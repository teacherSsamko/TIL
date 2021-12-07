a = int(input())  # 3digit num
B = input()
b = int(B)

B = list(B)

while B:
    print(a * int(B.pop()))

print(a * b)
