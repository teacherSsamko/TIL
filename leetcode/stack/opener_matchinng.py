test1 = "({[]})"  # 1
test2 = "({[)]"  # 0
test3 = "([]{()})"  # 1
test4 = "{[}"  # 0
test5 = "{[]"  # 0

pairs = {"{": "}", "[": "]", "(": ")"}

closers = ["}", "]", ")"]


def find_match(txt):
    closers_to_match = []
    for c in txt:
        if c in pairs:
            closers_to_match.append(pairs[c])
        elif c in closers:
            if c == closers_to_match.pop():
                continue
            else:
                return 0

    return 1 if not closers_to_match else 0


print(find_match(test1))
print(find_match(test2))
print(find_match(test3))
print(find_match(test4))
print(find_match(test5))
