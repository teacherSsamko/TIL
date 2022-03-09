test1 = "({[]})"  # 1
test2 = "({[)]"  # 0
test3 = "([]{()})"  # 1
test4 = "{[}"  # 0
test5 = "{[]"  # 0

pairs = {"{": "}", "[": "]", "(": ")"}


def is_valid(txt):
    closers_to_match = []
    for c in txt:
        if c in pairs:
            closers_to_match.append(pairs[c])
        elif c in pairs.values():
            if c == closers_to_match.pop():
                continue
            else:
                return 0

    return 1 if not closers_to_match else 0


print(is_valid(test1))
print(is_valid(test2))
print(is_valid(test3))
print(is_valid(test4))
print(is_valid(test5))
