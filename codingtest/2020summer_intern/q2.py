def solution(n):
    answer = 0

    answer = threepow(n).pop(n - 1)

    return answer

def threepow(n):
    powlist = []
    power = 0
    powlist.append(pow(3, power))
    while len(powlist) <= n:
        templist = powlist.copy()
        biggest = templist.pop()
        if templist:
            for i in templist:
                new_n = biggest + i
                powlist.append(new_n)
        power += 1
        powlist.append(pow(3, power))



    return powlist

print(threepow(4))
print(solution(4) == 9)

print(solution(11) == 31)