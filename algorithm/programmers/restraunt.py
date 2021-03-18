def solution(n, weak, dist):
    from itertools import permutations
    L = len(weak)
    cand = []
    weak_points = weak + [w+n for w in weak]
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start
            for friend in friends:
                position += friend
                if position < weak_points[i + L - 1]:
                    count += 1
                    postion = [w for w in weak_points[i+1:i+L]
                               if w > position][0]
                else:
                    cand.append(count)
                    break

    return min(cand) if cand else -1


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
ans = 1
print(solution(n, weak, dist))
