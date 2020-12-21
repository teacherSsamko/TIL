l, nameset = list(map(int, input().split())), input().split()
strokes = {
    'a': 3,
    'b': 2,
    'c': 1,
    'd': 2,
    'e': 4,
    'f': 3,
    'g': 1,
    'h': 3,
    'i': 1,
    'j': 1,
    'k': 3,
    'l': 1,
    'm': 3,
    'n': 2,
    'o': 1,
    'p': 2,
    'q': 2,
    'r': 2,
    's': 1,
    't': 2,
    'u': 1,
    'v': 1,
    'w': 1,
    'x': 2,
    'y': 2,
    'z': 1
}
a = list(nameset[0].lower())
b = list(nameset[1].lower())

mixed = []

x = 0
for i in range(max(l)):
    try:
        mixed.append(strokes[a.pop(0)])
    except Exception as e:
        pass
    try:
        mixed.append(strokes[b.pop(0)])
    except Exception as e:
        pass

# print(mixed)
result = mixed.copy()
while len(result) > 2:
    tmp = []
    for i in range(len(result) - 1):
        x = result[i] + result[i + 1]
        if x >= 10:
            x -= 10
        tmp.append(x)
    result = tmp

result = list(map(str, result))
result = ''.join(result)
print(f'{int(result)}%')
