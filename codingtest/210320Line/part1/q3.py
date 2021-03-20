def solution(enter, leave):
    answer = []
    meet_count = [0] * len(enter)
    meet_count = {x: set() for x in enter}
    # print(meet_count)
    idx = 0
    # room = [enter.pop(0)]
    room = []
    to_leave = None
    while leave:
        if not to_leave and leave:
            to_leave = leave.pop(0)
        if to_leave in room:
            del room[room.index(to_leave)]
            to_leave = None
            continue
        if enter:
            room.append(enter.pop(0))
        for person in room:
            meet_count[person] |= set(room)
    # print(meet_count)

    result = [(i, len(cnt) - 1) for i, cnt in meet_count.items()]
    result = sorted(result)
    # print(result)
    answer = list(map(lambda x: x[1], result))

    return answer


enters = [[1, 3, 2], [1, 4, 2, 3], [3, 2, 1], [3, 2, 1], [1, 4, 2, 3]]
leaves = [[1, 2, 3], [2, 1, 3, 4], [2, 1, 3], [1, 3, 2], [2, 1, 4, 3]]
result = [[0, 1, 1], [2, 2, 1, 3], [1, 1, 2], [2, 2, 2], [2, 2, 0, 2]]

for i in range(len(enters)):
    print(solution(enters[i], leaves[i]))
    # break
