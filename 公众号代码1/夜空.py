#参考来源：https://mp.weixin.qq.com/s?src=11&timestamp=1583487640&ver=2200&signature=YnhlFsQetekgf5vGj1t62LZsfPnLKS4uX3iS7fW-KQaSBGD17iiNTr9q0
#4BwQSwk0eJskH1NB25BUgxgIR4EwzzwZwRJKK42jQ-sLXC8N96OS*kKzQpb6jRbzshRn6Ce&new=1
from turtle import *
from random import random,randint

screen = Screen()
width ,height = 800,600
screen.setup(width,height)
screen.title("模拟3D星空_海龟画图版_作者:来源于网络_经过修改")
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)#这里要设为0，否则很卡

t = Turtle(visible = False,shape="circle")
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width/2,randint(-height/2,height/2))

stars = []
for i in range(200):
    star = t.clone()
    s =random()/3
    star.shapesize(s,s)
    star.speed(int(s*10))
    star.setx(width/2 + randint(1,width))
    star.sety( randint(-height/2,height/2))
    star.showturtle()
    stars.append(star)

while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor()<-width/2:
            star.hideturtle()
            star.setx(width/2 + randint(1,width))
            star.sety( randint(-height/2,height/2))
            star.showturtle()
