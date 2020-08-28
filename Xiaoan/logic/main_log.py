import time
from datetime import datetime
import draw


class MainLogic(object):

    def __init__(self):

        # 打开nc.txt文件
        with open("../data/nc.txt", 'r+', encoding="gbk") as f:
            line = f.read()
            self.x = eval(line)
        print("小安:欢迎进入小智能")
        c = self.x["你的名字"]
        print(f"小安:你好,{c}")

        # 创建菜单字典
        self.menu_logic = {}

        # 初始化子菜单
        self.menu_dic = {}

        # 初始化draw.py
        self.draw = draw.Draw()

    def nowtime(self):
        print(f"现在的时间是{datetime.now()}")

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

    @staticmethod
    def _merge(menu_1, menu_2):
        res = {**menu_1, **menu_2}
        return res

    def menu(self):
        """
        这里用于创建主要逻辑的菜单以及总菜单，在主要逻辑中添加方法后请务必在此添加菜单
        以及总菜单添加子菜单
        """
        self.menu_logic["现在时间"] = self.nowtime,
        self.menu_logic["删除所有记忆"] = self.delete_all

        # 将绘图的菜单加入到主菜单中
        self.menu_dic = self._merge(self.menu_logic, self.draw.menu_dict)

    def run(self):

        while True:
            # 主循环

            instruction = input("请输入指令：")

            # 程序退出
            quit = ["0", '退出程序', '退出', '退出小安', '小安退出', '小安退出程序']
            if instruction in quit:
                break

            # 生成菜单
            self.menu()
            # print(self.menu_dic.keys())


if __name__ == '__main__':
    log = MainLogic()
    log.run()
