import time
from datetime import datetime


class MainLogic(object):

    def __init__(self):

        # 打开nc.txt文件
        with open("../data/nc.txt", 'r+', encoding="utf-8") as f:
            line = f.read()
            self.x = eval(line)
        print("小安:欢迎进入小智能")
        c = self.x["你的名字"]
        print(f"小安:你好,{c}")

        # 初始化菜单字典
        self.menu_dict = {}

    def nowtime(self):

        return f"现在的时间是{datetime.now()}"

    def delete_all(self):
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

    def menu(self):
        self.menu_dict = {
            "现在时间": self.nowtime(),
            "删除所有记忆": self.delete_all()
        }

#     def run(self):
#
#         # 用于测试本文件的方法
#         self.nowtime()
#
#
# if __name__ == '__main__':
#     log = MainLogic()
#     log.run()
