import re

# 패턴에 매칭되는 모든 문자열 가져오기
print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))

# *, +와 그룹 활용하기
print(re.match('[a-z]+(.[a-z]+)*$', 'hello.world'))
print(re.match('[a-z]+(.[a-z]+)*$', 'hello.1234'))
print(re.match('[a-z]+(.[a-z]+)*$', 'hello'))
print()

# email 검증
valid_mail = re.compile('\w+@[a-z]+(\.[a-z]+)+$')
print(valid_mail.match('lu@gma.com'))
print(valid_mail.match('lu@gma.com.'))
print(valid_mail.match('lu@gma'))

