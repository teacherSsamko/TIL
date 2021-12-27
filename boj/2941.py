import re

r = re.compile(r'c=|c-|dz=|d-|lj|nj|s=|z=')

result = r.sub('1', input())

print(len(result))
