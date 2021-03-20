import re


def valid_program(program, cmd_program):
    return program == cmd_program


def valid_flag_type(type_checker, flag_arg):

    if isinstance(type_checker, list):
        # Check if numbers
        if isinstance(type_checker[0], int):
            # print("check numbers")
            for arg in flag_arg:
                try:
                    int(arg)
                except ValueError:
                    # print(arg)
                    return False
            return True
        else:
            # check if strings
            # print("check string")
            for arg in flag_arg:
                if not isinstance(arg, str):
                    print("arg")
                    return False
            return True
    else:
        if len(flag_arg) > 1:
            return False
        # CHECK IF NUMBER
        flag_arg = flag_arg.pop(0)

        if type_checker == 1:
            try:
                flag_arg = int(flag_arg)
            except ValueError:
                return False
        # check if string
        if type(type_checker) == type(flag_arg):
            return True
        return False


def set_rules(flag_rules):
    rules = dict()
    for flag_rule in flag_rules:
        k, v = flag_rule.split(" ")
        if v == "STRING":
            rules[k] = v
        elif v == "NUMBER":
            rules[k] = 1
        elif v == "NULL":
            rules[k] = None
        elif v == "NUMBERS":
            rules[k] = [1, 2]
        elif v == "STRINGS":
            rules[k] = ["a", "b"]

    return rules


def solution(program, flag_rules, commands):
    answer = []
    # flag에 해당하는 argument type을 확인하기 위해 flag_rule을 dictionary 형태로 저장
    rules = set_rules(flag_rules)
    # print(rules)

    # command 별로 validation check
    for command in commands:
        isValid = True
        cmds = command.split(" ")
        # program 이름 체크
        if not valid_program(program, cmds.pop(0)):
            isValid = False
            answer.append(isValid)
            continue

        # flag, flag_arg 검사
        flag_option = re.compile("-[0-9A-Za-z ]+")
        flag_cmds = flag_option.findall(" ".join(cmds))
        if not flag_cmds:
            answer.append(False)
            break
        for cmd in flag_cmds:
            cmd.rstrip(" ")
            # print(cmd)
            # flag가 -e 인지 검사
            if cmd.startswith("-e"):
                if len(cmd) == 2:
                    continue
                else:
                    isValid = False
                    break
            cmd = cmd.split()
            flag = cmd[0]
            flag_arg = cmd[1:]
            # 적합한 flag인지 검사
            # print(isValid)
            if not rules.get(flag):
                isValid = False
                break
            # 적합한 type인지 검사
            # print(isValid)
            if not valid_flag_type(rules[flag], flag_arg):
                isValid = False
                break

        answer.append(isValid)

    return answer


program = "line"
flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]
answer = [True, False]
print(solution(program, flag_rules, commands))

program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
answer = [False, True]
print(solution(program, flag_rules, commands))
