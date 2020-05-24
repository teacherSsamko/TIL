import turtle as t
import random as rd


t.speed(0)
for x in range(500):
    a = rd.randint(1,35)
    ang = rd.randint(1,359)

    t.forward(a)
    t.right(ang)
