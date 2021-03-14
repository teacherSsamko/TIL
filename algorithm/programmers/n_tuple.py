import re


def solution(s):
    def strtodict(s):
        # set_ = s.strip("\{\}")
        p = re.compile("{.*?}")
        set_ = p.findall(s)
        set_ = list(map(lambda x: x.strip("\{\}").split(","), set_))
        return set_
    answer = []
    set_ = strtodict(s)
    set_ = sorted(set_, key=len)
    for x in set_:
        new = set(x) - set(answer)
        answer.append(list(new).pop())
    answer = list(map(lambda x: int(x), answer))
    return answer


s = input()
print(solution(s))
