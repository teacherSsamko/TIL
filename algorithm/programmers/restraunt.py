def solution1(n, weak, dist):
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


def solution(n, weak, dist):
    W = len(weak)
    repair_l = [()]
    answer = 0
    dist.sort(reverse=True)

    for can_move in dist:
        repairs = []
        answer += 1

        for i, wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [w + n for w in weak[:i]]
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))
        # print(repairs)

        cand = set()
        for r in repairs:
            for x in repair_l:
                new = r | set(x)
                if len(new) == W:
                    print('ok', r, set(x))
                    return answer
                cand.add(tuple(new))
        repair_l = cand
        print(repair_l)


n = 12
weak = [1, 3, 4, 9, 10]
dist = [1, 2, 3, 4]
ans = 1
print(solution(n, weak, dist))
