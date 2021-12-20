s = list(input().lower())

alphabet = list(set(s))

if len(alphabet) == 1:
    print(s[0].capitalize())
else:
    count = {}

    for a in alphabet:
        count[a] = s.count(a)

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    if count[0][1] == count[1][1]:
        print('?')
    else:
        print(count[0][0].capitalize())
