"""
알파벳 받아서 조이스틱 최소 횟수 출력하기
JAZ = 12
JAN = 23
JEROEN = 56
AAAZ = 2
"""


def solution(name):
    def leftright(target, now, cursor):
        # right
        moveR = 0
        cursorR = cursor
        for i in range(cursor, len(target)):
            if target[i] != now[i]:
                cursorR = i
                moveR = i - cursor
                break
        # left
        moveL = 0
        cursorL = cursor
        while cursorL > -(len(target)):
            if target[cursorL] != now[cursorL]:
                break
            moveL += 1
            cursorL -= 1

        if moveL < moveR:
            return moveL, cursorL
        else:
            return moveR, cursorR

    answer = 0
    target = list(map(lambda x: ord(x), list(name)))
    print(target)
    now = [65 for i in range(len(target))]
    print(now)
    # updown
    for i in range(len(target)):
        answer += min(target[i] - now[i], 91 - target[i])

    # leftright
    cursor = 0
    while target != now:
        now[cursor] = target[cursor]
        move, cursor = leftright(target, now, cursor)
        answer += move

    return answer


n = input()
print(solution(n))
