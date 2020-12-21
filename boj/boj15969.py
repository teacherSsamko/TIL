import sys

# data = sys.stdin.readlines().split("\n")
n, scores = input(), list(map(int, input().split()))
# print(data)

# n = data[0]
# scores = list(map(int, data[1]))

min_s = min(scores)
max_s = max(scores)

print(max_s - min_s)
