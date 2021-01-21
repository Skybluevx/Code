def main():
    print("五子棋游戏".center(50, '='))
    guige = int(input("请输入棋盘的规格："))
    # 按照五子棋的棋盘样式，画出棋盘
    print_init(guige)

    # 初始化棋盘
    wzq = {}
    for i in range(1, guige + 1):
        for j in range(1, guige + 1):
            wzq[(i, j)] = "+"
    # 重画棋盘
    reprint(guige, wzq)
# 按照五子棋的棋盘样式，画出棋盘


def print_init(guige):
    # 打印出首行的棋盘列
    for i in range(guige):
        print("%4d" % (i + 1), end='')
    print()
    # 双重循环，第一重为棋盘的行，隔一行输出棋盘的行数
    for i in range(guige * 2 - 1):
        # 打印出类似 “1  +---+---+---+---+---+”，行号，+，—
        if (i % 2 == 0):
            print("%-3d" % ((i + 2) / 2), end='')
            # 第二重循环，为棋盘的列，主要在于找出对应位置显示的内容
            for j in range(guige * 4 - 3):
                if (j % 4 == 0):
                    print("+", end='')
                else:
                    print("-", end='')
        # 打印出类似“  |   |   |   |   |   |”
        else:
            print("%3s" % ' ', end='')
            for j in range(guige * 4 - 3):
                if (j % 4 == 0):
                    print("|", end='')
                else:
                    print(" ", end='')
        # 每行输出完成之后换行
        print()
# 重画棋盘，对双方下子进行重画


def reprint(guige, wzq):
    for i in range(guige * guige):
        if i % 2 == 0:
            xuanshou = "X"
        else:
            xuanshou = "O"
        # 双方轮流下棋
        while 1:
            print("现在轮到%s方落子" % xuanshou)
            print("请输入落子位置：")
            while True:
                try:
                    a = int(input("x="))
                    b = int(input("y="))
                except BaseException:
                    print("输入格式不正确，请重新输入！")
                    continue
                if a < 0 or b < 0 or a > guige or b > guige:
                    print("超出范围,请重新落子！")
                else:
                    break
            if wzq[(a, b)] in ["X", "O"]:
                print("您输入的位置有子，请重新输入！")
            else:
                break
        if wzq[(a, b)] == "+":
            # 重画棋盘
            wzq[(a, b)] = xuanshou
            for i in range(guige):
                print("%4d" % (i + 1), end='')
            print()
            for i in range(guige * 2 - 1):
                if (i % 2 == 0):
                    print("%-3d" % ((i + 2) / 2), end='')
                    for j in range(guige * 4 - 3):
                        if (j % 4 == 0):
                            x = (i + 2) / 2
                            y = j / 4 + 1
                            print(wzq[(x, y)], end='')
                        else:
                            print("-", end='')
                else:
                    print("%3s" % ' ', end='')
                    for j in range(guige * 4 - 3):
                        if (j % 4 == 0):
                            print("|", end='')
                        else:
                            print(" ", end='')
                print()
        else:
            isture = True
            print("您输入的位置已经有子，请重新输入！")
            # 判断输赢
        # 第一种情况
        wzq_win1(wzq, guige, xuanshou)
        # 第二种情况
        wzq_win2(wzq, guige, xuanshou)
        # 第三种情况
        wzq_win3(wzq, guige, xuanshou)
        # 第四种情况
        wzq_win4(wzq, guige, xuanshou)
    else:
        print("游戏结束，平局！")
# 判断输赢


def wzq_win1(wzq, guige, xuanshou):
    # 第一种输赢情况
    for i in range(1, guige + 1):
        for j in range(1, guige - 3):
            if (wzq[(i, j)] == wzq[(i, j + 1)] == wzq[(i, j + 2)] ==
                    wzq[(i, j + 3)] == wzq[(i, j + 4)] and wzq[(i, j)] in ["X", "O"]):
                print("%s获胜,游戏结束！" % xuanshou)
                exit()


def wzq_win2(wzq, guige, xuanshou):
    # 第二种输赢情况
    for i in range(1, guige - 3):
        for j in range(1, guige + 1):
            if (wzq[(i, j)] == wzq[(i + 1, j)] == wzq[(i + 2, j)] ==
                    wzq[(i + 3, j)] == wzq[(i + 4, j)] and wzq[(i, j)] in ["X", "O"]):
                print("%s获胜,游戏结束！" % xuanshou)
                exit()


def wzq_win3(wzq, guige, xuanshou):
    # 第三种输赢情况
    for i in range(1, guige - 3):
        for j in range(1, guige - 3):
            if (wzq[(i,
                     j)] == wzq[(i + 1,
                                 j + 1)] == wzq[(i + 2,
                                                 j + 2)] == wzq[(i + 3,
                                                                 j + 3)] == wzq[(i + 4,
                                                                                 j + 4)] and wzq[(i,
                                                                                                  j)] in ["X",
                                                                                                          "O"]):
                print("%s获胜,游戏结束！" % xuanshou)
                exit()


def wzq_win4(wzq, guige, xuanshou):
    # 第四种输赢情况
    for i in range(1, guige - 3):
        for j in range(5, guige + 1):
            if (wzq[(i,
                     j)] == wzq[(i + 1,
                                 j - 1)] == wzq[(i + 2,
                                                 j - 2)] == wzq[(i + 3,
                                                                 j - 3)] == wzq[(i + 4,
                                                                                 j - 4)] and wzq[(i,
                                                                                                  j)] in ["X",
                                                                                                          "O"]):
                print("%s获胜,游戏结束！" % xuanshou)
                exit()


main()
