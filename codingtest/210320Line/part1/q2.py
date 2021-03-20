def solution(inp_str):
    import re
    from collections import Counter
    from itertools import groupby
    answer = []
    length = len(inp_str)
    # filter 1
    if length < 8 or length > 15:
        answer.append(1)

    # filter 2
    p = re.compile('[a-zA-Z0-9~!@#$%^&*]+')
    # p = re.compile('[()-_=+]+')
    m = p.match(inp_str)
    if m and m.group() != inp_str:
        answer.append(2)

    # filter 3
    f1 = re.compile('[a-z]+')
    f2 = re.compile('[A-Z]+')
    f3 = re.compile('[0-9]+')
    f4 = re.compile('[!@#$%^&*]+')
    fs = [f1, f2, f3, f4]
    f_count = 0
    for f in fs:
        if f.search(inp_str):
            f_count += 1
    if f_count < 3:
        answer.append(3)

    # filter 4
    same_group = [len(list(g)) for k, g in groupby(inp_str)]
    same_count = max(same_group)
    if same_count > 3:
        answer.append(4)

    # filter 5
    same_counter = Counter(list(inp_str))
    for count in same_counter.values():
        if count > 4:
            answer.append(5)

    if not answer:
        answer.append(0)

    return answer


prohibit = "()-_=+"

inp_str = "AaTa+!12-3"
result = [2]

inp_strs = ["AaTa+!12-3", "aaaaZZZZ)",
            "CaCbCgCdC888834A", "UUUUU", "ZzZz9Z824"]
results = [[2], [2, 3, 4], [1, 4, 5], [1, 3, 4, 5], [0]]

for inp_str in inp_strs[:]:
    print(solution(inp_str))
