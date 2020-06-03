import re

# 연습문제: 이메일 주소 검사하기
p = re.compile('[\w\-\.\+\_]+@[\w\-\.\+\_]+(\.[a-z]+)+$')

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
 
for email in emails:
    print(p.match(email) != None, end=' ')

# 다른 풀이
# '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'