s = input()
s_l = list(s)
# 97 ~ 122
for i in range(97, 123):
    if chr(i) in s:
        print(s_l.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
