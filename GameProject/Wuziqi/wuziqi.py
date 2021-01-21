# -*- coding=utf-8 -*-
import random
import pygame
from pygame.locals import *

pygame.init()

space = 60  # 四周留下的边距
cell_size = 40  # 每个格子大小
cell_num = 15
grid_size = cell_size * (cell_num - 1) + space * 2  # 棋盘的大小
screencaption = pygame.display.set_caption('五子棋')
screen = pygame.display.set_mode((grid_size, grid_size))  # 设置窗口长宽

chess_arr = []
flag = 1  # 1黑 2白
game_state = 1  # 游戏状态1.表示正常进行 2.表示黑胜 3.表示白胜


def get_one_dire_num(lx, ly, dx, dy, m):
    tx = lx
    ty = ly
    s = 0
    while True:
        tx += dx
        ty += dy
        if tx < 0 or tx >= cell_num or ty < 0 or ty >= cell_num or m[ty][tx] == 0:
            return s
        s += 1


def check_win(chess_arr, flag):
    # 先定义一个15*15的全0的数组,不能用[[0]*cell_num]*cell_num的方式去定义因为一位数组会被重复引用
    m = [[0] * cell_num for i in range(cell_num)]
    for x, y, c in chess_arr:
        if c == flag:
            m[y][x] = 1  # 上面有棋则标1
    lx = chess_arr[-1][0]  # 最后一个子的x
    ly = chess_arr[-1][1]  # 最后一个子的y
    dire_arr = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, -1), (1, 1)],
                [(-1, 1), (1, -1)]]  # 4个方向数组,往左＋往右、往上＋往下、往左上＋往右下、往左下＋往右上，4组判断方向

    for dire1, dire2 in dire_arr:
        dx, dy = dire1
        num1 = get_one_dire_num(lx, ly, dx, dy, m)
        dx, dy = dire2
        num2 = get_one_dire_num(lx, ly, dx, dy, m)
        if num1 + num2 + 1 >= 5:
            return True

    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state == 1 and event.type == pygame.MOUSEBUTTONUP:  # 鼠标弹起
            x, y = pygame.mouse.get_pos()  # 获取鼠标位置
            xi = int(round((x - space) * 1.0 / cell_size))  # 获取到x方向上取整的序号
            yi = int(round((y - space) * 1.0 / cell_size))  # 获取到y方向上取整的序号
            if xi >= 0 and xi < cell_num and yi >= 0 and yi < cell_num and (
                    xi, yi, 1) not in chess_arr and (xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
                if check_win(chess_arr, flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1

    screen.fill((244, 164, 96))  # 将界面设置为蓝色

    for x in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x + space, 0 + space),
                         (x + space, cell_size * (cell_num - 1) + space), 1)
    for y in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0 + space, y + space),
                         (cell_size * (cell_num - 1) + space, y + space), 1)

    for x, y, c in chess_arr:
        chess_color = (30, 30, 30) if c == 1 else (225, 225, 225)
        pygame.draw.circle(
            screen, chess_color, [
                x * cell_size + space, y * cell_size + space], 16, 16)

    if game_state != 1:
        myfont = pygame.font.Font(None, 60)
        white = 210, 210, 0
        win_text = "%s win" % ('black' if game_state == 2 else 'white')
        textImage = myfont.render(win_text, True, white)
        screen.blit(textImage, (260, 320))

    pygame.display.update()  # 必须调用update才能看到绘图显示
