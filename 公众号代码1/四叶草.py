"""
    四叶草
"""
import turtle


# 设置主窗口的大小和位置
turtle.setup(1000, 1000, 200, 200)
# 设置画笔下落, 即准备开始绘制图案
turtle.pendown()
# 设置画笔的大小
turtle.pensize(10)
# 设置画笔的颜色
turtle.pencolor('green')


def draw_clover(radius, rotate):  # 参数radius控制叶子的大小,rotate控制叶子的旋转
    # 绘制四片叶子, 四个循环
    for i in range(4):
        # 设置每个叶子之间相隔的角度
        direction = i * 90
        # 设置画笔的角度, 即设置每一片叶子的角度
        turtle.seth(60 + direction + rotate)
        # 画笔前进指定的距离
        turtle.fd(4 * radius)

        # 两个循环用来绘制叶子的边缘
        for j in range(2):
            # 设置画笔角度, 即将准备绘制叶子边缘
            turtle.seth(90 + direction + rotate)
            # 绘制半圆
            turtle.circle(radius, 180)

        # 绘制画笔回来的角度
        turtle.seth(-60 + direction + rotate)
        # 画笔前进指定距离
        turtle.fd(4 * radius)

    # 设置画笔朝向位向下
    turtle.seth(-90)
    # 前进指定距离
    turtle.fd(6 * radius)


draw_clover(50, 45)
turtle.mainloop()
