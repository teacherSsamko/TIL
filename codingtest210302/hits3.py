import re


def divide_three(s):
    if not "1" in s:
        slots = len(s) - 1
        return (slots) * (slots - 1) // 2
    elif s.count("1") % 3 != 0:
        return 0
    else:
        count_of_section = s.count("1") // 3
        result = 1
        if count_of_section == 1:
            return get_result(s)
        else:
            s = s.strip("0")

            count_one = 0
            count_zero = 0
            zeros = list()
            for i in range(len(s)):
                if s[i] == "1":
                    if count_one == count_of_section:
                        count_one = 1
                        zeros.append(count_zero)
                        count_zero = 0
                    else:
                        count_one += 1
                elif count_one == count_of_section:
                    count_zero += 1
            for zero in zeros:
                if zero != 0:
                    result *= zero + 1

            return result


def get_result(s):
    p = re.compile("0+")
    zeros = p.findall(s)
    result = 1
    for zero in zeros:
        result *= len(zero) + 1
    return result


if __name__ == '__main__':
    s = input()
    print(divide_three(s))
