import re


def valid_program(program, cmd_program):
    return program == cmd_program


def valid_flag_type(type_checker, flag_arg):
    if type_checker == 1:
        # print(flag_arg)
        try:
            flag_arg = int(flag_arg)
            return True
        except ValueError:
            return False
    # print(flag_arg)
    # print(type_checker)
    if type(type_checker) == type(flag_arg):
        try:
            int(flag_arg)
            # print(flag_arg)
            return False
        except ValueError:
            return True


def set_rules(flag_rules):
    rules = dict()
    for flag_rule in flag_rules:
        k, v = flag_rule.split(" ")
        if v == "STRING":
            rules[k] = v
        elif v == "NUMBER":
            rules[k] = 1
        else:
            rules[k] = None
    return rules


def solution(program, flag_rules, commands):
    answer = []
    # flag에 해당하는 argument type을 확인하기 위해 flag_rule을 dictionary 형태로 저장
    rules = set_rules(flag_rules)

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
            # print(cmd)
            cmd.rstrip(" ")
            # print(cmd)
            # flag가 -e 인지 검사
            if cmd.startswith("-e"):
                if len(cmd) == 2:
                    continue
                else:
                    isValid = False
                    break
            flag, flag_arg = cmd.split()
            # 적합한 flag인지 검사
            if not rules.get(flag):
                isValid = False
                break
            # 적합한 type인지 검사
            if not valid_flag_type(rules[flag], flag_arg):
                isValid = False
                break

        answer.append(isValid)

    return answer


program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]
answer = [True, False]
# print(solution(program, flag_rules, commands))

commands = ["line -s 123 -n HI", "line fun"]
answer = [False, False]
print(solution(program, flag_rules, commands))
