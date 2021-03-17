from copy import deepcopy


def turn(heading):
    heading = (heading + 1) % 4
    return heading


def move_forward(loc, heading):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    newLoc = deepcopy(loc)
    newLoc[0] += dx[heading]
    newLoc[1] += dy[heading]
    return newLoc


def check_move(loc, size):
    if 0 <= loc[0] and loc[0] <= size[0] and 0 <= loc[1] and loc[1] <= size[1]:
        return True
    else:
        return False


def p1(loc, heading, size):
    newLoc = move_forward(loc, heading)
    if not check_move(newLoc, size):
        return False
    heading = turn(heading)
    return [newLoc, heading]


def p2(loc, heading, size):
    heading = turn(heading)
    newLoc = move_forward(loc, heading)
    if not check_move(newLoc, size):
        return False
    return [newLoc, heading]


def p3(loc, heading, size):
    heading = turn(heading)
    return [loc, heading]


def solution(n, m, x, y):
    answer = 0
    depth = 0
    to_visit = list()
    to_visit.append([[0, 0], 0, depth])
    size = (n, m)
    target = [x, y]
    while to_visit:
        loc, heading, depth = to_visit.pop(0)
        if loc == target:
            # print("end", loc, target)
            break
        answer += 1
        depth += 1
        p1_loc = p1(loc, heading, size)
        if p1_loc:
            p1_loc.append(depth)
            to_visit.append(p1_loc)
        p2_loc = p2(loc, heading, size)
        if p2_loc:
            p2_loc.append(depth)
            to_visit.append(p2_loc)
        p3_loc = p3(loc, heading, size)
        if p3_loc:
            p3_loc.append(depth)
            to_visit.append(p3_loc)

    return depth


n, m, x, y = list(map(int, input().split()))
print(solution(n, m, x, y))

"""
1,1,1,1 > 3
5,5,3,3 > 8
"""
