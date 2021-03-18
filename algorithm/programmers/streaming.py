def solution(genres, plays):
    from collections import defaultdict
    import heapq
    answer = []
    h = defaultdict(list)
    genre_sum = defaultdict(int)
    genre_rank = list()
    #
    for i in range(len(genres)):
        heapq.heappush(h[genres[i]], (-plays[i], i))
        genre_sum[genres[i]] += plays[i]

    for k, v in genre_sum.items():
        heapq.heappush(genre_rank, (-v, k))
    print(h)
    for total_play, genre in genre_rank:
        for i in range(2):
            try:
                answer.append(heapq.heappop(h[genre])[1])
            except:
                continue

    print(genre_sum)
    print(genre_rank)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "pop", "dance"]
plays = [500, 600, 150, 500, 2500, 700, 30]
ans = [4, 1, 3, 0]

print(solution(genres, plays))
