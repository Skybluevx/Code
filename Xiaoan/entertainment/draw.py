import turtle as t


class Draw(object):

    def __init__(self):

        # 初始化菜单字典
        self.menu_dict = {
            "正方形": [self.zfx],
            "三角形": [self.sjx],
            "无角正方形": [self.wjzfx],
            "太阳花": [self.tyh],
            "五角星": [self.wjx],
            "六角形": [self.ljx],
            "叠加等边三角形": [self.djdbsjx],
            "圆": [self.yuan],
            "靶盘": [self.bp],
            "正方形螺旋线": [self.zfxlxx],
            "田字格": [self.tzg],
            "蟒蛇": [self.ms],
            "直线": [self.xian],
            "画板": [self.huaban],
        }

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

    # 画板
    def huaban(self):
        while True:
            print("小安:请输入画笔大小,输入help查看功能")
            hbaz = input("我:")
            if hbaz == 'help':
                print(
                    "小安:1.向右\n2.向左\n3.向前\n4.抬笔\n5.落笔\n6.清空\n7.画笔颜色\n8.到达坐标\n9.画圆\n10.背景颜色\n11.角度")
            else:
                t.pensize(int(hbaz))
                break
        while True:
            print("小安:请输入画笔的运动,输入“退出”退出")
            hb = input("我:")
            if hb == '向右':
                print("小安:请输入移动像素")
                hby = int(input("我:"))
                t.right(hby)
            elif hb == '向左':
                print("小安:请输入移动像素")
                hbz = int(input("我:"))
                t.left(hbz)
            elif hb == '向前':
                print("小安:请输入移动像素")
                hbq = int(input("我:"))
                t.fd(hbq)
            elif hb == '抬笔':
                t.penup()
            elif hb == '落笔':
                t.pendown()
            elif hb == '清空':
                self.cc()
            elif hb == '画笔颜色':
                print("小安:请输入画笔颜色,仅限英文\n如:red(红色),green(绿色),black(黑色),yellow(黄色),white(白色),grey(灰色),darkgreen(深绿色),gold(金色),violet(紫罗兰),purple(紫色)")
                hbys = input("我:")
                t.pencolor(hbys)
            elif hb == '退出':
                print("小安:退出")
                break
            elif hb == '到达坐标':
                print("小安:请输入第一个数字")
                hbzb = int(input("我:"))
                print("小安:请输入第二个数字")
                hbzb_2 = int(input("我:"))
                t.goto(hbzb, hbzb_2)
            elif hb == '画圆':
                print("小安:请输入圆的半径")
                hbyuan = input("我:")
                t.circle(int(hbyuan))
            elif hb == '背景颜色':
                windowe = t.Screen()
                print("小安:请输入背景颜色,仅限英文\n如:red(红色),green(绿色),black(黑色),yellow(黄色),white(白色),grey(灰色),darkgreen(深绿色),gold(金色),violet(紫罗兰),purple(紫色)")
                hbbj = input("我:")
                windowe.bgcolor(hbbj)
            elif hb == '角度':
                hbjd = int(input())
                t.seth(hbjd)
            else:
                print("输入错误")
