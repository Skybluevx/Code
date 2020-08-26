

class MainLogic(object):

    def __init__(self):

        # 打开nc.txt文件
        with open("df/nc.txt", 'r+') as f:
            line = f.read()
            self.x = eval(line)
        print("小安:欢迎进入小智能")
        c = self.x["你的名字"]
        print(f"小安:你好,{c}")

    def run(self):
        pass


if __name__ == '__main__':
    log = MainLogic()
    log.run()
