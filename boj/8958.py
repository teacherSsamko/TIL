rep = int(input())

for _ in range(rep):
    score = 0
    ox = input().split("X")
    for o in ox:
        n = len(o)
        score += n * (n + 1) // 2
    print(score)
