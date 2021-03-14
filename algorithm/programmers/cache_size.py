def solution(cacheSize, cities):
    from collections import deque

    answer = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5

    return answer


cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco",
          "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))
