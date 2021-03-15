def solution(clothes):
    from collections import defaultdict
    answer = 1
    closet = defaultdict(list)
    for cloth in clothes:
        closet[cloth[1]].append(cloth[0])
    for items in closet.values():
        answer *= len(items) + 1
    return answer - 1


def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for item, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution2(clothes))
