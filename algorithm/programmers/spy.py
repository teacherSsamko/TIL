def solution(clothes):
    from collections import defaultdict
    answer = 1
    closet = defaultdict(list)
    for cloth in clothes:
        closet[cloth[1]].append(cloth[0])
    for items in closet.values():
        answer *= len(items) + 1
    return answer - 1


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
