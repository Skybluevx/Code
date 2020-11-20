"""
    绘制五角星
"""
# 导入 turtle 库
import turtle

# 设置画笔的粗细
turtle.pensize(5)
# 设置画笔颜色,第一个为画笔的颜色,第二个位要填充的颜色
turtle.color("brown", "red")
# 在绘制要填充的形状之前要调用
turtle.begin_fill()
# 因为要画五条边,所以循环五次
for i in range(5):
    # 画笔向前走200
    turtle.forward(200)
    # 画笔右转144度
    turtle.right(144)
# 结束填充
turtle.end_fill()
# 作为一个 turtle 程序的结束语句,否则会出现画完图后直接闪退的情况
turtle.mainloop()
