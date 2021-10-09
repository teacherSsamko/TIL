def solution(p):
    answer = 0
    while True:
        p += 1
        if chk_beauty(p):
            return p


    return answer

def chk_beauty(year):
    str_year = str(year)
    set_year = set(str_year)
    if len(str_year) == len(set_year):
        return True

    return False

test1 = 2015
print(solution(test1))