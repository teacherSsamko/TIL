import re

# URL 판단 정규표현
p = re.compile('^https*://([a-zA-Z0-9-]+\.)+[a-zA-Z0-9]+(/[a-zA-Z0-9-_.?=]+)*')

print(p.match('http://www.example.com/hello/world.do?key=python'))
print(p.match('https://example/hello/world.html'))

url = input()

def valid_url(url):
    p = re.compile('^https?://([a-zA-Z0-9-]+\.)+[a-zA-Z0-9]+(/[a-zA-Z0-9-_.?=]+)*')

    if p.match(url):
        return True
    else:
        return False

print(valid_url(url))