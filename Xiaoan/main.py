from other import jingdutiao
from logic import main_log


def hello():

    print("小安：欢迎进入小智能")


def main():

    # 显示加载进度条
    # jingdutiao.jingdutiao()

    # 加载主要逻辑
    log = main_log.MainLogic()
    log.run()


if __name__ == "__main__":
    main()
