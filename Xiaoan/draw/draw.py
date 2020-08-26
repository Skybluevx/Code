import turtle as t


class Draw(object):

    def cc(self):
        # 定义画板还原

        t.clear()
        t.pensize(4)
        t.pencolor("black")
        t.penup()
        t.goto(0, 0)
        t.pendown()

    def zfx(self):
        # 画正方形

        self.cc()
        for i in range(4):
            t.fd(200)
            t.left(90)

    def sjx(self):
        # 画三角形

        self.cc()
        for i in range(3):
            t.fd(200)
            t.left(120)

    def wjzfx(self):
        # 画无角正方形

        self.cc()
        for i in range(4):
            t.penup()
            t.fd(50)
            t.pendown()
            t.fd(100)
            t.penup()
            t.fd(50)
            t.left()

    def tyh(self):
        self.cc()
        t.color("red", "yellow")
        t.begin_fill()
        while True:
            t.fd(200)
            t.left(170)
            if abs(t.pos()):
                break
        t.end_fill()
        t.done()
