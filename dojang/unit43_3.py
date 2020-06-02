import re

# 매칭 그룹
m = re.match('([0-9]+) ([0-9]+)', '10 295')
print(m.group(1))
print(m.group(2))
print(m.group())
print(m.group(0))

# 그룹 이름 지정하기
m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
print(m.group('func'))
print(m.group('arg'))