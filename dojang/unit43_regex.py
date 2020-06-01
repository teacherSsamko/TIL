import re

print(re.match('Hello', 'Hello, world!'))
print(re.match('Python', 'Hello, world!'))

print(re.search('^Hello', 'Hello, world!'))
print(re.search('world!$', 'Hello, world!'))
print(re.search('world$', 'Hello, world!'))

print(re.match('hello|world', 'hello'))