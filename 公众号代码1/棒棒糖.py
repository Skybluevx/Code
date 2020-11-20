#参考来源：https://mp.weixin.qq.com/s?src=11&timestamp=1583495886&ver=2200&signature=x3jiWcb29p6Ec7kg1iLUGY1uHliMifSQZzuypvg41qQ9YzQbTMD2LSzo-ggGWr
#FiLaIhlF0ObK-NeydraaRxd0nz4qE4Y5LMMDQrmFOFSFydyZQepbdPDtetpt4ukpMe&new=1
import turtle
import time
colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
turtle.bgcolor('black')


for x in range(36):
    t.pencolor (colors[x%6])
    t.width(100)
    t.forward(8.5)
    t.left(10)

t.right(90)

for y in range(100):
    t.pencolor (colors[y%6])
    t.width(20)
    t.forward(2)

for x in range(18):
    t.pencolor (colors[x%6])
    t.width(20)
    t.forward(8.5)
    t.left(10)

time.sleep(10)
