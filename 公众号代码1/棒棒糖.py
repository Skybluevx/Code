"""
    棒棒糖
"""
# 导入 turtle 库
import turtle

# 设置棒棒糖所需要的颜色
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# 定义一支画笔
t = turtle.Pen()
# 设置画布的颜色
turtle.bgcolor('black')
# 设置画笔的粗细
t.width(100)

# 循环36次, 每次向左旋转10度, 这里画的是棒棒糖的最大的糖的部分
for x in range(36):
    # 设置画笔的颜色, 从 color 中循环选取
    t.pencolor(colors[x % 6])
    # 每次画笔前进8.5的距离
    t.forward(8.5)
    # 画笔向左旋转10度
    t.left(10)

# 画笔右转90度
t.right(90)
# 设置画笔的颜色
t.width(20)

# 循环100次, 绘制棒棒糖棒子直的部分
for y in range(100):
    # 循环设置画笔的颜色
    t.pencolor(colors[y % 6])
    # 每次循环画笔前进2
    t.forward(2)

# 循环18次, 绘制棒棒糖棒子的弯曲部分
for x in range(18):
    # 循环设置画笔的颜色
    t.pencolor(colors[x % 6])
    # 每次循环前进8.5
    t.forward(8.5)
    # 每次循环左转10度
    t.left(10)

# 作为一个 turtle 程序的结束语句,如果不加会出现画完图后直接闪退的情况
turtle.mainloop()
