#参考来源：https://blog.csdn.net/weixin_44523387/article/details/94555249

import turtle
import time
turtle.pensize(5)
turtle.color("brown","red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
    turtle.end_fill()
    time.sleep(2)
turtle.mainloop()
