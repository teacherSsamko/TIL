# 범위 판단하기
import re

# *: 0개 이상, +: 1개 이상
print(re.match('[0-9]*', '1234'))
print(re.match('[0-9]+', '1234'))
print(re.match('[0-9]+', 'abcd'))

print(re.match('a*b', 'b'))
print(re.match('a+b', 'b'))
print(re.match('a*b', 'aab'))
print(re.match('a+b', 'aab'))
print()

print(re.match('abc?d', 'abd'))
print(re.match('abc?d', 'abcd'))
print(re.match('abc?d', 'abccd'))
print(re.match('ab[0-9]?c', 'ab3c'))
print(re.match('ab.d', 'abxd'))
print()

print(re.match('h{3}', 'hhhello'))
print(re.match('(hello){3}', 'hellohellohelloworld'))
print()

# 전화번호 형식
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-100'))
print()

print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-100-1000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-10-1000'))