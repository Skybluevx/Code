from random import randint


class LuckTest(object):

    def __init__(self):
        self.menu_dict = {
            "运气测试": [self.lucktest],
        }

    @staticmethod
    def lucktest():
        print("小安:欢迎进入")
        while True:
            sls = 1
            try:
                yc = int(input("小安:请输入一个数字,需在1~20之间,输入“101”退出\n我:"))
            except:
                yc = 0
                print("小安:请输入数字")
            if yc == 101:
                print("小安:退出")
                break
            while True:
                yc_2 = randint(1, 20)
                if yc < 0 or yc > 20:
                    print("小安:输入错误")
                    break
                if yc != yc_2:
                    sls += 1
                else:
                    print("小安:你所输入的数字用了{}次中了".format(sls))
                    if sls < 20:
                        print("小安:你本次的运气贼好")
                    elif 21 > sls < 50:
                        print("小安:你本次的运气一般")
                    else:
                        print("小安:你本次的运气不够好")
                    sls = 1
                    break
