import re

# 특수 문자 판단하기
print(re.search('\*+', '1 ** 2'))
print(re.match('[$()a-zA-Z0-9]+', '$(document)'))
print()

# 문자, 숫자 shortcut
print(re.match('\d+', '1234'))
print(re.match('\D+', 'hello'))
print(re.match('\D+', 'hello12'))
print(re.match('\D+', '12'))

# 공백 처리하기
print(re.match('[a-zA-Z0-9 ]+', 'Hello 1234'))
print(re.match('[a-zA-Z0-9\s]+', 'Hello 1234'))

# 정규표현식 저장하기
p = re.compile('[0-9]+')
print(p.match('1234'))
print(p.search('hello'))