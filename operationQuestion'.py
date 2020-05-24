import random


def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + "+"

    if op == 2:
        q = q + "-"

    if op == 3:
        q = q + "*"

    q = q + str(b)

    return q

#anwer count
sc1 = 0

#incorrect count
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = int(input("="))

    if eval(q) == ans:
        print("correct")
        sc1 += 1

    else:
        print("incorrect")
        sc2 += 1


print("correct:", sc1, "incorrect: ", sc2)
if sc2 == 0:
    print("you are genius")
