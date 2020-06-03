import re

# 문자열 바꾸기
print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))
print(re.sub('[0-9]+', 'n', '1 2 fizz 4 buzz fizz 7 8'))

# 교체 함수 지정
def multiple10(m):
    n = int(m.group())
    return str(n * 10)

print(re.sub('[0-9]+', multiple10, '1 2 fizz 4 buzz fizz 7 8'))

print(re.sub('[0-9]+', lambda m: str(int(m.group()) * 10), '1 2 fizz 4 buzz fizz 7 8'))

