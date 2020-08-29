from random import randint


class MiniGame(object):

    def __init__(self):

        # 创建菜单
        self.menu_dict = {
            "猜数字": [self.guss_the_number],
            "石头剪刀布": [self.rps_game],
        }

    @staticmethod
    def guss_the_number():
        print("小安:欢迎进入")
        g = 0
        while True:
            try:
                print("小安:请选择难度\n1.简单 2.普通 3. 困难 4.自定义 5.输入退出退出")
                xq = input("我:")
                if xq == '1' or xq == '简单':
                    jd = randint(1, 20)
                    while True:
                        try:
                            print("小安:请输入,它在1~20")
                            sh = int(input("我:"))
                            if sh == jd:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif sh < jd:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except:
                            print("小安:输入错误")
                elif xq == '2' or xq == '普通':
                    pt = randint(1, 50)
                    while True:
                        try:
                            print("小安:请输入,它在1~50")
                            shf = int(input("我:"))
                            if shf == pt:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shf < pt:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except:
                            print("小安:输入错误")
                elif xq == '3' or xq == '困难':
                    kn = randint(1, 100)
                    while True:
                        try:
                            shy = int(input("小安:请输入,它在1~100"))
                            if shy == kn:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shy < kn:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except:
                            print("小安:输入错误")
                elif xq == '4' or xq == '自定义':
                    print("小安:请输入范围,第一个数字和第二个数字用“，”隔开")
                    zdy, wwa = eval(input("我:"))
                    cszz = randint(zdy, wwa)
                    while True:
                        try:
                            print("小安:请输入,它在{}~{}".format(zdy, wwa))
                            shyq = int(input("我:"))
                            if shyq == cszz:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shyq < cszz:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except:
                            print("小安:输入错误")
                elif xq == '5' or xq == '退出':
                    print("小安:退出猜数字")
                    break
                else:
                    print("小安:输入错误")
            except:
                print("小安:输入错误")

    @staticmethod
    def rps_game():
        print("小安:石头为１，剪刀为２，布为３,记得只能输入数字哦\n"
              "输入45退出")
        print("小安:来吧")
        while True:
            try:
                jd = randint(1, 3)
                jd_1 = int(input("我:"))
                if jd == 1 and jd_1 == 1:
                    print("小安:我出的也是石头,嘻嘻")
                elif jd == 1 and jd_1 == 2:
                    print("小安:我出的是石头,我赢了")
                elif jd == 1 and jd_1 == 3:
                    print("小安:我出的是石头,emmm你赢了")
                elif jd == 2 and jd_1 == 1:
                    print("小安:我出的是剪刀,emmm你赢了")
                elif jd == 2 and jd_1 == 2:
                    print("小安:我出的也是剪刀,嘻嘻")
                elif jd == 2 and jd_1 == 3:
                    print("小安:我出的是剪刀,我赢了")
                elif jd == 3 and jd_1 == 1:
                    print("小安:我出的是布,我赢了")
                elif jd == 3 and jd_1 == 2:
                    print("小安:我出的是布,emmm你赢了")
                elif jd == 3 and jd_1 == 3:
                    print("我出的也是布,嘻嘻")
                elif jd_1 == 45:
                    print("小安:退出")
                    break
                else:
                    print("小安:出错了")
            except:
                print("小安:输入错误,请重新输入")
