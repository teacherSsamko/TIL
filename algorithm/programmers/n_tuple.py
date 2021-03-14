def solution(s):
    import re
    from collections import Counter

    c = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True)]))


s = input()
print(solution(s))
