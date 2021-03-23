def solution(doc, word):
    answer = 0
    cursor = doc.find(word)
    if cursor == -1:
        return answer

    while cursor < len(doc):
        answer += 1
        cursor += len(word)
        tmp = doc[cursor:].find(word)
        if tmp == -1:
            break
        cursor += tmp

    return answer


doc = input()
word = input()
print(solution(doc, word))
