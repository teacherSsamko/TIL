# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def convert_to_ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(nums)

def convert_to_decimal(n: str):
    nums = []
    n = list(n)
    i = 0
    while n:
        nums.append(int(n.pop()) * (3**i))
        i += 1
    return sum(nums)
    

def solution(n):
    # convert to ternary
    # filp it
    ternary = convert_to_ternary(n)
    # conver to decimal
    
    return convert_to_decimal(ternary)