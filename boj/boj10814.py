persons = list()
for i in range(int(input())):
    age, name = input().split()
    persons.append((int(age), i, name))

result = sorted(persons, key=lambda x: x[0])
for r in result:
    print(f'{r[0]} {r[2]}')
