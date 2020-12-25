N = int(input())
S = input()

bonus = 0

total = 0

for i, x in enumerate(S):
    if ord(x) == 79:
        total += i + bonus + 1
        bonus += 1
    else:
        bonus = 0

print(total)
