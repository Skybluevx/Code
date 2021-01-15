#https://blog.csdn.net/qq_41575507/article/details/97174850?depth_1-utm
#_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

import turtle as t
 
def moveto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
 
 
t.setup(width=1000,height=700)
t.pensize(3)
t.color('black','orange')
#t.hideturtle()
moveto(0,-300)
t.circle(300)
t.speed(16)
t.begin_fill()
t.fillcolor()
t.circle(300)
t.end_fill()
 
 
#左眼睛
#t.hideturtle()
t.speed(1)
moveto(-200, 50)
t.color('darkorange')
t.begin_fill()
t.fillcolor("white")
t.pensize(6)
t.seth(30)
t.circle(-240, 40)
t.seth(40)
t.circle(30,90)
t.seth(158)
t.circle(180,70)
t.seth(280)
t.circle(30,86)
t.end_fill()
moveto(-180, 63)
t.color("black")
t.pensize(1)
t.begin_fill()
t.fillcolor("black")
t.circle(22)
t.end_fill()
 
 
 
#右眼睛
moveto(50, 80)
t.color('darkorange')
t.begin_fill()
t.fillcolor("white")
t.pensize(6)
t.seth(20)
t.circle(-240, 40)
t.seth(40)
t.circle(30,90)
t.seth(150)
t.circle(180,70)
t.seth(280)
t.circle(30,86)
t.end_fill()
moveto(70, 86)
t.color("black")
t.pensize(1)
t.begin_fill()
t.fillcolor("black")
t.circle(22)
t.end_fill()
 
 
 
# 嘴巴
t.speed(1)
moveto(-200, -60)
t.pensize(10)
t.color("brown")
t.seth(-70)
t.circle(215,150)
 
#眉毛
t.color("black")
moveto(-200,160)
t.seth(60)
t.circle(-100,40)
t.circle(-50,90)
 
moveto(50,160)
t.seth(60)
t.circle(-100,40)
t.circle(-50,90)
 
t.done()
