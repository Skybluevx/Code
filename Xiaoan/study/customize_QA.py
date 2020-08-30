import time
from datetime import datetime


class CustomizeQA(object):

    def __init__(self):

        self.menu_dict = {
            "自定义问答": [self.customize]
        }

        # 打开nc.txt文件
        with open("data/nc.txt", 'r+', encoding="gbk") as f:
            line = f.read()
            self.x = eval(line)

    @staticmethod
    def nowtime():
        print(f"现在的时间是{datetime.now()}")

    @staticmethod
    def delete_all():
        # 删除数据文件中的所有字典
        result = input("请输入“确认”来确认本次操作，否则请输入“否”")
        if result == "确认":
            print("小安正在删除记忆中...")
            for i in range(101):
                print("\r{:3}%".format(i), end='')
                time.sleep(0.05)
            print("删除完毕...")

            with open("nc.txt", "w") as f:
                pass
        if result == "否":
            print("本次操作取消...")

    def customize(self):
        print("小安:欢迎进入小智能自定义问答")
        c = self.x["你的名字"]
        print(f"小安:你好,{c}")
        y = input("我:")
        if y in self.x:
            d = self.x["{}".format(y)]
            print("小安:{}".format(d))  # 输出键的对应值
        elif '现在时间' in y:  # 如果‘现在时间在用户输入里面执行’
            self.nowtime()
        elif "在吗" in y:
            print("小安:我一直都在")
        elif '你会什么' in y:
            print("小安:我会")
            for key in self.x:
                print(key)
        elif '删除所有记忆' == y:  # 删除字典
            self.delete_all()
        elif '删除问题' == y:  # 删除字典中的一个键对值
            y_3 = input("小安:你确定吗")
            if '是' in y_3:
                y_4 = input("小安:请输入你想要删除的问题")
                print("删除中...")
                for i in range(101):
                    print("\r{:3}%".format(i), end='')
                    time.sleep(0.05)
                print("小安:删除完毕")
                del self.x["{}".format(y_4)]
                with open("nc.txt", "w") as f:
                    f.write(str(self.x))
        else:
            print("小安:emmm,我无法回答")  # 机器人学习
            print("小安:是否需要我学习?")
            s = input("我:")
            while True:
                if '是' in s:
                    s_1 = input("小安:请输入你的问题")
                    s_2 = input("小安:请输入你的希望得到的回答")
                    self.x[s_1] = s_2
                    print("小安:已学习完毕")
                    with open("df/nc.txt", 'w') as f:
                        f.write(str(self.x))
                    break
                elif '否' in s or '不' in s:
                    print("小安:那好吧")
                    break
                else:
                    print("小安:请回答我的问题,是否需要我学习")
                    s = input("我:")
