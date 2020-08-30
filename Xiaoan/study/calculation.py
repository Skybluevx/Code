import math
from datetime import datetime
from random import randint
from PIL import Image, ImageFilter, ImageEnhance


class Math(object):

    def __init__(self):
        # 创建菜单
        self.menu_dict = {
            "计算机": [self.computer],
            "九九乘法表": [self.jiujiu],
            "图片修改": [self.magic_fix],
            "速算": [self.speed_calcu],
        }

    @staticmethod
    def computer():
        print(
            "小安:我只会二则运算，嘻嘻\n"
            "乘号用‘*’除号用‘/’\n"
            "乘方用‘**’,第一个数字是x次幂\n"
            "计算绝对值用/x/,第二个数字填0\n"
            "计算阶乘用!,仅限正整数和０，第二个数字填0\n"
            "求一个数的平方根用/**/，第二个数字用０\n"
            "求一个数的平方根用“///”,第一个数是被开方数，第二个是次方\n"
            "计算俩个数之商的余数用“%”\n"
            "在符号里输入'[退出]'退出,第一和第二个数字填0")
        while True:
            try:
                print("小安:请输入第一个数字")
                js = int(input("我:"))
                print("小安:请输符号")
                js_2 = input("我:")
                print("小安:请输入第二个数字")
                js_3 = int(input("我:"))
                if js_2 == '+':
                    jg = js + js_3
                    print(jg)
                elif js_2 == '-':
                    jg_2 = js - js_3
                    print(jg_2)
                elif js_2 == '*':
                    jg_3 = js * js_3
                    print(jg_3)
                elif js_2 == '/':
                    jg_4 = js / js_3
                    print(jg_4)
                elif js_2 == '**':
                    jg_5 = pow(js, js_3)
                    print(jg_5)
                elif js_2 == '/x/':
                    jg_6 = math.fabs(js)
                    print(jg_6)
                elif js_2 == '!':
                    jg_7 = math.factorial(js)
                    print(jg_7)
                elif js_2 == '/**/':
                    jg_8 = math.sqrt(js)
                    print(jg_8)
                elif js_2 == '///':
                    jg_9 = pow(js, 1 / js_3)
                    print(jg_9)
                elif js_2 == '%':
                    jg_10 = js % js_3
                    print(jg_10)
                elif js_2 == '[退出]':
                    print("小安:已退出")
                    break
                else:
                    print("小安:不会")
            except BaseException:
                print("小安:输入错误,请重新输入")

    @staticmethod
    def jiujiu():
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("{}x{}={:2} ".format(j, i, i * j), end='')
            print('')

    @staticmethod
    def magic_fix():
        print("小安:我会设置图片的\n"
              "1.轮廓效果\n"
              "2.对比度增强")
        tp = input("我:")
        if tp == '轮廓效果':
            tp_1 = input("小安:请输入文件名(需把需修改的文件放在与程序相同的目录下)")
            tp_2 = input("小安:请输入需保存的文件名")
            im = Image.open('{}.jpg'.format(tp_1))
            om = im.filter(ImageFilter.CONTOUR)
            om.save('{}.jpg'.format(tp_2))
        elif tp == '对比度增强':
            tp_3 = input("小安:请输入文件名(需把需修改的文件放在与程序相同的目录下)")
            tp_4 = input("小安:请输入需保存的文件名")
            tp_5 = eval(input("小安:请输入对比度"))
            im_2 = Image.open('{}.jpg'.format(tp_3))
            om_2 = ImageEnhance.Contrast(im_2)
            om_2.enhance(tp_5).save('{}.jpg'.format(tp_4))
        else:
            print("小安:我不会")

    @staticmethod
    def speed_calcu():
        fs = 0
        now = datetime.now()
        while True:
            print("小安:请选择难度\n1.简单\t2.困难\n输入'666'退出")
            x1 = input("我:")
            if x1 == '1' or x1 == '简单':
                while True:
                    jd = randint(0, 10)
                    jd_1 = randint(0, 10)
                    jd_2 = randint(1, 2)
                    if jd_2 == 1:
                        print("小安:{}+{}=".format(jd, jd_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        jd_4 = int(input("我:"))
                        jd_3 = jd + jd_1
                        if jd_3 == jd_4:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif jd_4 == 999:
                            print("小安:退出简单模式")
                            break
                        elif jd_4 == 333:
                            zc = open("zc.txt", "a+")
                            zc_1 = ["难度:简单 分数:{:2}\t保存时间:{}\n".format(fs, now)]
                            zc.writelines(zc_1)
                            for line in zc:
                                print(line)
                                zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
                    else:
                        print("小安:{}-{}=".format(jd, jd_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        jd_5 = int(input("我:"))
                        jd_6 = jd - jd_1
                        if jd_5 == jd_6:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif jd_5 == 999:
                            print("小安:退出简单模式")
                            break
                        elif jd_5 == 333:
                            zc = open("zc.txt", "a+")
                            zc_1 = ["难度:简单 分数:{:2}\t保存时间:{}\n".format(fs, now)]
                            zc.writelines(zc_1)
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
            elif x1 == '2' or x1 == '困难':
                while True:
                    kn = randint(10, 20)
                    kn_1 = randint(10, 20)
                    kn_2 = randint(1, 2)
                    if kn_2 == 1:
                        print("小安:{}+{}=".format(kn, kn_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        kn_3 = int(input("我:"))
                        if kn_3 == kn + kn_1:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif kn_3 == 999:
                            print("小安:退出困难模式")
                            break
                        elif kn_3 == 333:
                            zc = open("zc.txt", "a+")
                            zc.write("难度:困难 分数:{:2}\t保存时间:{}\n".format(fs, now))
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
                    else:
                        print("小安:{}-{}=".format(kn, kn_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        kn_5 = int(input("我:"))
                        kn_6 = kn - kn_1
                        if kn_5 == kn_6:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif kn_5 == 999:
                            print("小安:退出困难模式")
                            break
                        elif kn_5 == 333:
                            zc = open("zc.txt", "a+")
                            zc.write("难度:困难 分数:{:2}\t保存时间:{}\n".format(fs, now))
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("当前分数:{}".format(fs))
            elif x1 == '666' or x1 == '６６６':
                print("小安:退出")
                break
            else:
                print("小安:输入错误")
