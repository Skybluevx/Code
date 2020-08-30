

class Caesar(object):

    def __init__(self):
        self.menu_dict = {
            "凯撒密码": [self.caesar]
        }

    @staticmethod
    def caesar():
        while True:
            ks = input("\n小安:请输入\n1.加密 2.解密 3.退出\n我:")
            if ks == '1' or ks == '加密':
                jm = input("\n小安:请输入需加密的内容\n我:")
                try:
                    jm_1 = int(input("\n小安:请输入密匙\n我:"))
                except BaseException:
                    print("小安:密匙输入错误,密匙必须是数字")
                print("小安:加密结果是")
                for p in jm:
                    if ord("a") <= ord("p") <= ord("z"):
                        jmjg = chr(ord("a") + (ord(p) - ord("a") + jm_1) % 26)
                        print("{}".format(jmjg), end='')
                    else:
                        print("{}".format(p))
            elif ks == '2' or ks == '解密':
                jm_3 = input("\n小安:请输入需解密的内容\n我:")
                try:
                    jm_4 = int(input("\n小安:请输入密匙\n我:"))
                except BaseException:
                    print("小安:密匙输入错误,密匙必须是数字")
                print("小安:解密结果是")
                for p in jm_3:
                    if ord("a") <= ord("p") <= ord("z"):
                        jmjg_1 = chr(
                            ord("a") + (ord(p) - ord("a") - jm_4) % 26)
                        print("{}".format(jmjg_1), end='')
                    else:
                        print("{}".format(p), end='')
            elif ks == '3' or ks == '退出':
                print("小安:退出凯撒密码")
                break
            else:
                print("小安:输入错误")
