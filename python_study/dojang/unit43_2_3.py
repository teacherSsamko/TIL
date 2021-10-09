import re

# 숫자와 영문 조합
print(re.match('[a-zA-Z0-9]+', 'Hello1234'))
print(re.match('[a-zA-Z0-9]+', 'Hello'))
print(re.match('[A-Z0-9]+', 'hello'))
print(re.match('[가-힣]+', '홍길동'))

# 부정 표현하기
print(re.match('[^A-Z]+', 'Hello'))
print(re.match('[^0-9]+', 'Hello'))
print(re.match('[^A-Z]+', 'hello'))
print()

# 시작 검사하기
print(re.search('^[A-Z]+', 'Hello'))

# 끝 검사하기
print(re.search('[0-9]+$', 'hello1234'))