def solution(N, M, cards):
    from itertools import combinations
    answer = 0
    card_set = combinations(cards, 3)
    min_gap = M
    for card_ in card_set:
        gap = M - sum(card_)
        if gap >= 0 and gap < min_gap:
            answer = sum(card_)
            min_gap = gap
    return answer


N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
print(solution(N, M, cards))
