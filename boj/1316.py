n = int(input())
result = 0

for _ in range(n):
    word = input()
    new_word = ""
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        new_word += word[i]
    new_word += word[-1]

    if len(set(new_word)) == len(new_word):
        result += 1
print(result)
