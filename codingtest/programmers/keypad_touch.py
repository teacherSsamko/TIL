# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    def find_pos(val):
        keypads = [
            [1,2,3], 
            [4,5,6], 
            [7,8,9], 
            ["*",0,"#"]
        ]
        r, c = 0, 0
        for i, row in enumerate(keypads):
            if val in row:
                r = i
                for j, col in enumerate(row):
                    if val == col:
                        c = j
        return r, c
            
            
    def get_distance(curr, target):
        curr_r, curr_c = find_pos(curr)
        target_r, target_c = find_pos(target)

        return abs(curr_r - target_r) + abs(curr_c - target_c)

    answer = ''
    L_nums = [1,4,7]
    R_nums = [3,6,9]
    curr_pos_L = "*"
    curr_pos_R = "#"
    for n in numbers:
        # add L
        if n in L_nums:
            answer += "L"
            curr_pos_L = n
            continue
        # add R
        if n in R_nums:
            answer += "R"
            curr_pos_R = n
            continue
        # Center row
        dist_L = get_distance(curr_pos_L, n)
        dist_R = get_distance(curr_pos_R, n)
        if dist_L < dist_R:
            answer += "L"
            curr_pos_L = n
        elif dist_L > dist_R:
            answer += 'R'
            curr_pos_R = n
        else:
            if hand == "left":
                answer += "L"
                curr_pos_L = n
            else:
                answer += 'R'
                curr_pos_R = n
    return answer