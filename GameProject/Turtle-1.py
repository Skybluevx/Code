import turtle as t


t.speed("normal")
t.bgcolor("black")
t.pensize(25)
t.pencolor("red")
i = 0

while i < 10:
    t.penup()
    t.goto(-63, -10)
    t.forward(100)
    t.pendown()
    t.forward(300)
    t.left(20)
