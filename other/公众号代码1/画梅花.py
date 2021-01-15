#参考来源：https://blog.csdn.net/wei_zhen_dong/article/details/102750308

"""
author:魏振东
data：2019.10.25
func:绘制创意图形
"""

from turtle import *
from random import *

#画雪花
def drawSnow():
    hideturtle()
   
    pensize(2)
    for i in range(20):
        pencolor("white")
        penup()
        setx(randint(-640,640))
        sety(randint(-400,400))
        pendown()
        dens=randint(8,12)
        snowsize=randint(10,14)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)
# 位移函数
def gotopos(x, y):
    up()
    goto(x, y)
    down()
    ht()

def apply_rules(path, rules):
    L = [_ for _ in path]
    for i in range(len(L)):
        symbol = L[i]
        if symbol == 'F':
            L[i] = rules[symbol]
        if symbol == 'X':
            L[i] = rules[symbol]
    path = ''.join(L)
    return path


def draw_path(path):
    posList, angleList = [], []
    for symbol in path:
        if symbol == 'F':
            forward(length)
        elif symbol == '+':
            left(angle)
        elif symbol == '-':
            rt(angle)
        elif symbol == '[':
            posList.append(pos())
            angleList.append(heading())
        elif symbol == 'a':
            pensize(3)
            color("black")
        elif symbol == 'b':
            pensize(2)
            color("black")
        elif symbol == 'c':
            pensize(2)
            color("black")
        elif symbol == ']':
            up()
            home()
            goto(posList.pop())
            left(angleList.pop())
            down()

# 写字
def writez(x, y, str_, size=56, font="华文行楷"):
    gotopos(x, y)
    write(str_, font=(font, size))

# 画布
setup(1280, 800)
speed(0)
bgcolor("Silver")

# 题字
color("black")
writez(-213, -210, "梅", 196)
writez(-50, 100, "宋")
writez(80, 20, "王")
writez(33, -30, "安", 62)
writez(-18, -95, "石", 78)

# 写诗
color("black")
s = "墙角数枝梅"
s2 = "凌寒独自开"
s3 = "遥知不是雪"
s4 = "为有暗香来"
for i in range(len(s)):
    writez(560, 350 - i * 50, s[i], 36)
for i in range(len(s2)):
    writez(510, 320 - i * 50, s2[i], 36)
for i in range(len(s3)):
    writez(460, 290 - i * 50, s3[i], 36)
for i in range(len(s4)):
    writez(410, 260 - i * 50, s4[i], 36)

# 画雪
drawSnow()

# 画梅
gotopos(249, -26)
speed(0)
gotopos(-650, -100)
length = 6
path = 'F'
angle = 27
rules = {
    'F': 'aFF[b-F++F][c+F--F]c++F--F',
    'X': 'aFF+[b+F]+[c-F]'
}
for _ in range(4):
    path = apply_rules(path, rules)
draw_path(path)
done()

