import turtle as t

def f():
    t.setheading(90)
    t.forward(10)

def r():
    t.setheading(0)
    t.forward(10)

def l():
    t.setheading(180)
    t.forward(10)

def b():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(r, "Right")
t.onkeypress(l, "Left")
t.onkeypress(b, "Down")
t.onkeypress(f, "Up")

t.onkeypress(blank, "Escape")
t.onscreenclick(t.goto)
t.write("HEllo")
t.listen()
