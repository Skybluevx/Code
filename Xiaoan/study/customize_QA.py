import time
from datetime import datetime
import sqlite3


class CustomizeQA(object):

    def __init__(self):

        self.menu_dict = {
            "自定义问答": [self.customize]
        }
        self.x = {
            "你的名字": "小安",
        }

        # 连接数据库文件
        self.conn = sqlite3.connect("../data/Q_A.db")
        self.cur = self.conn.cursor()
        # 创建表
        self.cur.execute("CREATE TABLE IF NOT EXISTS q_a (question TEXT, answer TEXT)")

        # 初始化自定义问答的菜单
        self.menu = None

    # 结束的时候关闭数据库的链接
    def __del__(self):
        self.cur.close()
        self.conn.close()

    @staticmethod
    def nowtime():
        print(f"现在的时间是{datetime.now()}")

    def update_menu(self):
        self.cur.execute("SELECT question FROM q_a")
        que = []
        for i in self.cur:
            que.append(i[0])
        # print(que)
        return que

    def customize(self):
        print("小安:欢迎进入小智能自定义问答")
        c = self.x["你的名字"]
        print(f"小安:你好,{c}")
        while True:
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
                questions = self.cur.execute("SELECT question FROM q_a")
                for question in questions:
                    print(question[0])
            elif '删除所有记忆' == y:  # 删除字典
                self.cur.execute("DROP TABLE q_a")
                self.conn.commit()
            elif '删除问题' == y:  # 删除字典中的一个键对值
                y_3 = input("小安:你确定吗")
                if '是' in y_3:
                    y_4 = input("小安:请输入你想要删除的问题")
                    print("删除中...")
                    try:
                        self.cur.execute("DELETE FROM q_a WHERE question=?", y_4)
                        self.conn.commit()
                    except:
                        print("没有这个问题哦，请确定输入的问题是否存在或文字是否有错误~~")
                    print("小安:删除完毕")
            elif y in self.update_menu():
                try:
                    answer = self.cur.execute("SELECT answer FROM q_a WHERE question=?", (y,))
                    for i in answer:
                        print(i[0])
                except:
                    pass
            elif y == "退出":
                print("自定义问答结束")
                break
            else:
                print("小安:emmm,我无法回答")  # 机器人学习
                print("小安:是否需要我学习?")
                s = input("我:")
                while True:
                    if '是' in s:
                        s_1 = input("小安:请输入你的问题")
                        s_2 = input("小安:请输入你的希望得到的回答")
                        self.cur.execute("INSERT INTO q_a VALUES (?, ?)", (s_1, s_2))
                        self.conn.commit()
                        print("小安:已学习完毕")
                        break
                    elif '否' in s or '不' in s:
                        print("小安:那好吧")
                        break
                    else:
                        print("小安:请回答我的问题,是否需要我学习")
                        s = input("我:")


if __name__ == '__main__':
    ex = CustomizeQA()
    ex.customize()
