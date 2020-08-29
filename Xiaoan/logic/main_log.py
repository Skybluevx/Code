import time
from datetime import datetime
import draw
import calculation
import mini_game


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

        # 初始化其他功能
        self.draw = draw.Draw()
        self.mini_game = mini_game.MiniGame()
        self.calculation = calculation.Math()

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

    def print_menu(self):
        """
        创建菜单并输出
        """
        menu_dict = self.menu()
        print("   |")
        for key in menu_dict.keys():
            print(f"   |--[{key}]")

    def menu(self):
        """
        这里用于创建主要逻辑的菜单以及总菜单，在主要逻辑中添加方法后请务必在此添加菜单

        ****笔记****
        **问题**
          将各个功能封装成方法时，可以通过将各个方法写入一个字典的形式来简化调用，即将每个
        函数作为字典的value，并给予每个value一个key，从而实现通过匹配key来调用各个功能，
        这个方法在调用其他功能时得以成功使用，但是在主逻辑功能中则出现了问题。

        **解决**
          通过debug可知主逻辑方法调用时各个方法都是以tuple的形式存在，因此在 执行方法 那
        一步通过添加索引来完成成功调用；但是，值得注意的是，添加索引的地方必须是 执行方法
        那个地方，而直接在菜单字典中添加就不行，从而导致了其他功能菜单制作的时候需要将每个
        方法放入列表中。
        """
        self.menu_logic["1"] = self.print_menu,
        self.menu_logic["现在时间"] = self.nowtime,
        self.menu_logic["删除所有记忆"] = self.delete_all

        """
        在其他文件创建其他功能时请记得在此将相关功能的菜单添加至总菜单中
        """
        menu_dic = self._merge(self.menu_logic, self.draw.menu_dict)
        menu_dic = self._merge(menu_dic, self.mini_game.menu_dict)
        menu_dic = self._merge(menu_dic, self.calculation.menu_dict)

        return menu_dic

    def run(self):

        while True:
            # 主循环

            ins = input("请输入指令：")

            # 程序退出
            quit = ["0", '退出程序', '退出', '退出小安', '小安退出', '小安退出程序']
            if ins in quit:
                break

            # 执行方法
            menu_dict = self.menu()
            try:
                menu_dict[ins][0]()
            except KeyError:
                print("指令输入有误/暂无此指令，请输入[菜单]获取菜单栏。")


if __name__ == '__main__':
    log = MainLogic()
    log.run()
