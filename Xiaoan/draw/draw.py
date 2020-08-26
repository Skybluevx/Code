import turtle as t


class Draw(object):

    @staticmethod
    def cc():
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
            t.left(90)

    def tyh(self):
        # 定义太阳花

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

    def wjx(self):
        # 定义画五角星
        self.cc()
        t.fillcolor('red')
        t.begin_fill()
        while True:
            t.fd(200)
            t.right(144)
            if abs(t.pos()) < 1:
                break
        t.end_fill()

    def ljx(self):
        # 定义画六角形
        self.cc()
        t.left(120)
        t.fd(150)
        t.left(120)
        t.fd(150)
        t.left(120)
        t.fd(100)
        t.left(60)
        t.fd(100)
        t.left(120)
        t.fd(150)
        t.left(120)
        t.fd(150)
        t.left(120)
        t.fd(50)
        t.right(60)
        t.fd(50)

    def djdbsjx(self):
        # 定义画叠加等边三角形
        self.cc()
        t.fd(200)
        t.left(120)
        t.fd(200)
        t.left(120)
        t.fd(100)
        t.left(120)
        t.fd(100)
        t.right(120)
        t.fd(100)
        t.right(120)
        t.fd(100)
        t.left(120)
        t.fd(100)

    def yuan(self):
        # 定义画圆
        self.cc()
        t.pensize(5)
        t.circle(100)

    def bp_2(self, bp_3):
        t.penup()
        t.goto(0, bp_3)
        t.pendown()

    def bp(self):  # 定义画靶盘
        self.cc()
        t.pensize(5)
        t.circle(100)
        self.bp_2(-100)
        t.circle(200)
        self.bp_2(-200)
        t.circle(300)

    def zfxlxx(self):  # 定义画正方形螺旋线
        self.cc()
        t.speed(60)
        t.pensize(2)
        for x in range(100):
            t.fd(2 * x)
            t.left(90)
        t.done()

    @staticmethod
    def tzg_1():
        print("+ - - - - + - - - - +")

    @staticmethod
    def tzg_2():
        print("l         l         l")

    def tzg(self):  # 定义画田字格
        self.tzg_1()
        self.tzg_2()
        self.tzg_2()
        self.tzg_2()
        self.tzg_2()
        self.tzg_1()
        self.tzg_2()
        self.tzg_2()
        self.tzg_2()
        self.tzg_2()
        self.tzg_1()

    # 定义画蟒蛇
    def ms(self):
        self.cc()
        t.setup(650, 350, 200, 200)
        t.penup()
        t.fd(-250)
        t.pendown()
        t.pensize(25)
        t.pencolor("purple")
        t.seth(-40)
        for i in range(4):
            t.circle(40, 80)
            t.circle(-40, 80)
        t.circle(40, 80 / 2)
        t.fd(40)
        t.circle(16, 180)
        t.fd(40 * 2 / 3)

    # 定义画线
    def xian(self):
        self.cc()
        t.fd(200)
