import os
import requests
from datetime import *
from tkinter import *  # 导入tkinter库
from time import *
from turtle import *
from math import *
from random import *
from playsound import *
from tqdm import *
import urllib.request
import urllib.parse
import json
import re
import hashlib
from datetime import datetime
import pygame
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

key = '1f136301d56d4df482527d838f862573'


def get_songs_info(search_song) -> dict:
    url = 'https://autumnfish.cn/search?keywords={}'.format(search_song)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    try:
        con = requests.get(url=url, headers=headers).json()
        songs = con['result']['songs']
    except Exception as e:
        print('查找出错', e)
    else:
        songs_list = []
        for song in songs:
            songs_info = {
                'song_id': song['id'],
                'song_name': song['name'],
                'song_singer': song['artists'][0]['name']}
            songs_list.append(songs_info)

        for index, s in enumerate(songs_list):
            print('第{}: 歌手: {}'.format(index + 1, s["song_singer"]))

        try:
            num = int(input('你需要第几首:'))
        except BaseException:
            print('输入错误  将随机下载一首')
            return random.choice(songs_list)
        else:
            if num <= 0 or num > len(songs_list):
                print('输入数值不在范围  将随机下载一首')
                return random.choice(songs_list)
            return songs_list[num - 1]


def dow_song(song_id, song_name):
    song_id = str(song_id)
    song_name = song_name

    song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    con = requests.get(url=song_down_link, headers=headers).content

    if not os.path.exists('df/缓存歌曲'):
        os.mkdir('df/缓存歌曲')

    try:
        with open('df/缓存歌曲/{}.mp3'.format(song_name), 'wb') as fq:
            fq.write(con)
            fq.flush()
            print('{}缓存完成'.format(song_name))
    except Exception as e:
        print('{}缓存出错,错误信息:{}'.format(song_name, e))


def main(equation):  # 方程组求解主函数
    equation = equation.lower()
    equa_mid = equation.split(",")  # 把输入的字符串用逗号转换成两个方程的列表
    equa_mid[0] = equa_mid[0].replace("x-", "x+-")  # 对方程1进行规整，方便后面识别X，Y前面的数字
    equa_mid[1] = equa_mid[1].replace("x-", "x+-")  # 对方程2进行规整，方便后面识别X，Y前面的数字
    # 以下几行对方程1和方程2进行规整，识别出X和Y前面的系数
    # 把+作为标识符进行分裂方程，mid1，mid2方程1识别出的中间数据。mid3和mid4位方程2识别出的中间数据
    mid1 = equa_mid[0].split("+")
    mid2 = mid1[1].split("=")
    mid3 = equa_mid[1].split("+")
    mid4 = mid3[1].split("=")
    if mid1[0][:-1] == "-":  # 由于减号和1系统无法直接识别，所以进行转换，-换成-1，x前面没有数字时需要换成1X。对X和Y进行同样的操作。
        mid1[0] = "-1x"
    elif mid1[0][:-1] == "":
        mid1[0] = "1x"
    if mid2[0][:-1] == "-":
        mid2[0] = "-1y"
    elif mid2[0][:-1] == "":
        mid2[0] = "1y"
    if mid3[0][:-1] == "-":
        mid3[0] = "-1x"
    elif mid3[0][:-1] == "":
        mid3[0] = "1x"
    if mid4[0][:-1] == "-":
        mid4[0] = "-1y"
    elif mid4[0][:-1] == "":
        mid4[0] = "1y"
    equa1 = [mid1[0], mid2[0], mid2[1]]  # 规整后的方程1的列表
    equa2 = [mid3[0], mid4[0], mid4[1]]  # 规整后的方程2的列表
    a = eval(equa1[0][:-1])  # 从方程1中识别出a和b
    b = eval(equa1[1][:-1])
    c = eval(equa2[0][:-1])  # 从方程2中识别出c和d
    d = eval(equa2[1][:-1])
    e = eval(equa1[2])  # 从方程1中识别出e
    f = eval(equa2[2])  # 从方程2中识别出f
    y = (a * f - c * e) / (a * d - b * c)  # 用二元一次方程组的公式计算x，y
    x = (d * e - b * f) / (a * d - b * c)
    return x, y


def cc():  # 定义画板还原
    clear()
    pensize(4)
    pencolor("black")
    penup()
    goto(0, 0)
    pendown()


def zfx():  # 定义画正方形
    cc()
    for i in range(4):
        fd(200)
        left(90)


def sjx():  # 定义画三角形
    cc()
    for i in range(3):
        fd(200)
        left(120)


def wjzfx():  # 定义画无角正方形
    cc()
    for i in range(4):
        penup()
        fd(50)
        pendown()
        fd(100)
        penup()
        fd(50)
        left(90)


def tyh():  # 定义画太阳花
    cc()
    color('red', 'yellow')
    begin_fill()
    while True:
        fd(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


def wjx():  # 定义画五角星
    cc()
    fillcolor('red')
    begin_fill()
    while True:
        fd(200)
        right(144)
        if abs(pos()) < 1:
            break
    end_fill()


def ljx():  # 定义画六角形
    cc()
    left(120)
    fd(150)
    left(120)
    fd(150)
    left(120)
    fd(100)
    left(60)
    fd(100)
    left(120)
    fd(150)
    left(120)
    fd(150)
    left(120)
    fd(50)
    right(60)
    fd(50)


def djdbsjx():  # 定义画叠加等边三角形
    cc()
    fd(200)
    left(120)
    fd(200)
    left(120)
    fd(100)
    left(120)
    fd(100)
    right(120)
    fd(100)
    right(120)
    fd(100)
    left(120)
    fd(100)


def yuan():  # 定义画圆
    cc()
    pensize(5)
    circle(100)


def bp_2(bp_3):
    penup()
    goto(0, bp_3)
    pendown()


def bp():  # 定义画靶盘
    cc()
    pensize(5)
    circle(100)
    bp_2(-100)
    circle(200)
    bp_2(-200)
    circle(300)


def zfxlxx():  # 定义画正方形螺旋线
    cc()
    speed(60)
    pensize(2)
    for x in range(100):
        fd(2 * x)
        left(90)
    done()


def tzg_1():
    print("+ - - - - + - - - - +")


def tzg_2():
    print("l         l         l")


def tzg():  # 定义画田字格
    tzg_1()
    tzg_2()
    tzg_2()
    tzg_2()
    tzg_2()
    tzg_1()
    tzg_2()
    tzg_2()
    tzg_2()
    tzg_2()
    tzg_1()

# 定义画蟒蛇


def ms():
    cc()
    setup(650, 350, 200, 200)
    penup()
    fd(-250)
    pendown()
    pensize(25)
    pencolor("purple")
    seth(-40)
    for i in range(4):
        circle(40, 80)
        circle(-40, 80)
    circle(40, 80 / 2)
    fd(40)
    circle(16, 180)
    fd(40 * 2 / 3)

# 定义画线


def xian():
    cc()
    fd(200)


for i in tqdm(range(100), ncols=62, desc='加载中'):
    sleep(0.05)
print("加载完毕\n")

x = {'你的名字': '我的名字是安'}
with open("df/nc.txt", 'r+') as f:  # 打开nc.txt文件
    line = f.read()
    x = eval(line)
print("小安:欢迎进入小智能")
c = x["你的名字"]
print("小安:你好,{}".format(c))
while 1 == 1:
    y = input("我:")
    if y in x:
        d = x["{}".format(y)]
        print("小安:{}".format(d))  # 输出键的对应值
    elif '现在时间' in y:  # 如果‘现在时间在用户输入里面执行’
        sj = datetime.now()
        sj_2 = sj.strftime("%Y-%m-%d %H:%M:%S")
        print("小安:现在时间是{}".format(sj_2))
    elif "在吗" in y:
        print("小安:我一直都在")
    elif '你会什么' in y:
        print("小安:我会")
        for key in x:
            print(key)
    elif '删除所有记忆' == y:  # 删除字典
        y_2 = input("小安:你确定吗")
        if '是' in y_2:
            print("删除中...")
            for i in range(101):
                print("\r{:3}%".format(i), end='')
                sleep(0.05)
            print("小安:删除完毕")
            x.clear()
            with open("nc.txt", "w") as f:
                f.write(str(x))
        if '否' in y_2:
            print("小安:嗯")
    elif '删除问题' == y:  # 删除字典中的一个键对值
        y_3 = input("小安:你确定吗")
        if '是' in y_3:
            y_4 = input("小安:请输入你想要删除的问题")
            print("删除中...")
            for i in range(101):
                print("\r{:3}%".format(i), end='')
                sleep(0.05)
            print("小安:删除完毕")
            del x["{}".format(y_4)]
            with open("nc.txt", "w") as f:
                f.write(str(x))
    elif '画画' == y:  # 如果用户输入等于‘画画’执行
        print("小安:我会画\n1.正方形\n2.三角形\n3.无角正方形\n4.太阳花\n5.五角星\n6.六角形\n7.叠加等边三角形\n8.圆\n9.靶盘\n10.正方形螺旋线\n11.田字格\n12.蟒蛇\n13.直线")
        print("小安:你希望我画什么?")
        y_1 = input("我:")
        if y_1 == '正方形':
            zfx()
        elif y_1 == '三角形':
            sjx()
        elif y_1 == '无角正方形':
            wjzfx()
        elif y_1 == '太阳花':
            tyh()
        elif y_1 == '五角星':
            wjx()
        elif y_1 == '六角形':
            ljx()
        elif y_1 == '叠加等边三角形':
            djdbsjx()
        elif y_1 == '圆':
            yuan()
        elif y_1 == '靶盘':
            bp()
        elif y_1 == '正方形螺旋线':
            zfxlxx()
        elif y_1 == '田字格':
            tzg()
        elif y_1 == '蟒蛇':
            ms()
        elif y_1 == '直线':
            xian()
        else:
            print("小安:这个我不会画")
    elif "打开文件" in y:
        dk = input("小安:你是要打开文件吗?")
        if dk == '是':
            dk_1 = input("小安:请输入你要打开的文件(需包含文件的路径)")
            os.system("{}".format(dk_1))
        elif dk == '否':
            print("小安:哦")
        else:
            print("小安:输入错误")
    elif y == '退出程序' or y == '退出' or y == '退出小安' or y == '小安退出' or y == '小安退出程序':
        break
    elif y == '高级计算':
        print(
            "小安:我只会二则运算，嘻嘻\n乘号用‘*’除号用‘/’\n乘方用‘**’,第一个数字是x次幂\n计算绝对值用/x/,第二个数字填0\n计算阶乘用!,仅限正整数和０，第二个数字填0\n求一个数的平方根用/**/，第二个数字用０\n求一个数的平方根用“///”,第一个数是被开方数，第二个是次方\n计算俩个数之商的余数用“%”\n在符号里输入'[退出]'退出,第一和第二个数字填0")
        while True:
            try:
                js = input("小安:请输入,列:1+1,2*8\n我:")
                if '+' in js:
                    js_1, js_2 = js.split(sep='+')
                    js_3 = eval(js_1) + eval(js_2)
                    print(js_3)
                elif '-' in js:
                    js_1, js_2 = js.split(sep='-')
                    js_3 = eval(js_1) - eval(js_2)
                    print(js_3)
                elif '*' in js:
                    js_1, js_2 = js.split(sep='*')
                    js_3 = eval(js_1) * eval(js_2)
                    print(js_3)
                elif '/' in js:
                    js_1, js_2 = js.split(sep='/')
                    js_3 = eval(js_1) / eval(js_2)
                    print(js_3)
                elif '**' in js:
                    js_1, js_2 = js.split(sep='**')
                    js_3 = eval(js_1) ** eval(js_2)
                    print(js_3)
                elif 'fabs' in js:
                    js_1, js_2 = js.split(sep='fabs')
                    js_3 = fabs(eval(js_2))
                    print(js_3)
                elif '!' in js:
                    js_1, js_2 = js.split(sep='!')
                    js_3 = factorial(eval(js_1))
                    print(js_3)
                elif 'sqrt' in js:
                    js_1, js_2 = js.split(sep='sqrt')
                    js_3 = sqrt(eval(js_2))
                    print(js_3)
                elif '%' in js:
                    js_1, js_2 = js.split(sep='%')
                    js_3 = eval(js_1) % eval(js_2)
                    print(js_3)
                elif '退出' in js:
                    break
                else:
                    print("小安:错误")
            except BaseException:
                print("小安:输入错误,请重新输入")
    elif y == 'PM2.5值':
        while True:
            try:
                pm = eval(input("小安:请输入PM2.5数值,输入字母退出"))
                if 0 <= pm < 35:
                    print("小安:空气质量优，快去户外运动吧！")
                elif 35 <= pm < 75:
                    print("小安:空气质量良好，适度户外运动")
                else:
                    print("小安:空气污染，请小心！")
            except BaseException:
                print("小安:退出")
                break
    elif y == '九九乘法表':
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("{}x{}={:2} ".format(j, i, i * j), end='')
            print('')
    elif y == '正负数辩别':
        while True:
            try:
                zfs = int(input("小安:请输入一个数字,输入字母退出"))
                if zfs < 0:
                    print("小安:这是负数")
                elif zfs > 0:
                    print("小安:这是正数")
                else:
                    print("小安:这是０")
            except BaseException:
                print("小安:退出")
                break
    elif y == '图片修改':
        print("小安:我会设置图片的\n1.轮廓效果\n2.对比度增强\n3.修改图片大小")
        tp = input("我:")
        if tp == '轮廓效果' or tp == '1':
            tp_1 = input("小安:请输入文件名(需把需修改的文件放在与程序相同的目录下)")
            tp_2 = input("小安:请输入需保存的文件名")
            im = Image.open('{}.jpg'.format(tp_1))
            om = im.filter(ImageFilter.CONTOUR)
            om.save('{}.jpg'.format(tp_2))
        elif tp == '对比度增强' or tp == '2':
            tp_3 = input("小安:请输入文件名(需把需修改的文件放在与程序相同的目录下)")
            tp_4 = input("小安:请输入需保存的文件名")
            tp_5 = eval(input("小安:请输入对比度"))
            im_2 = Image.open('{}.jpg'.format(tp_3))
            om_2 = ImageEnhance.Contrast(im_2)
            om_2.enhance(tp_5).save('{}.jpg'.format(tp_4))
        elif tp == '3' or tp == '修改图片大小':
            xgtp_1 = input("小安:请输入文件名(需把需修改的文件放在与程序相同的目录下)")
            xgtp__ = input("小安:请输入需保存的文件名")
            xgtp, xgtp_0 = eval(input("小安:请输入尺寸,如'12,12'"))
            xgtp_2 = Image.open("{}.jpg".format(xgtp_1)).resize((xgtp, xgtp_0))
            xgtp_2.save("{}.jpg".format(xgtp__))
        else:
            print("小安:我不会")
    elif y == '计算BMI值':
        print("小安:请输入身高(米)和体重(公斤)[逗号隔开]")
        height, weight = eval(input("我:"))
        bmi = weight / pow(height, 2)
        print("小安:BMI数值为:{:.2f}".format(bmi))
        if bmi < 18.5:
            who, dom = "偏瘦", "偏瘦"
        elif 18.5 <= bmi < 24:
            who, dom = "正常", "正常"
        elif 24 <= bmi < 25:
            who, dom = "正常", "偏胖"
        elif 25 <= bmi < 28:
            who, dom = "偏胖", "偏胖"
        elif 28 <= bmi < 30:
            who, dom = "偏胖", "肥胖"
        else:
            who, dom = "肥胖", "肥胖"
        print("小安:BMI指标为国际'{0}',国内'{1}'".format(who, dom))
    elif y == '猜数字':
        print("小安:欢迎进入")
        g = 0
        while True:
            try:
                print("小安:请选择难度\n1.简单 2.普通 3. 困难 4.自定义 5.输入退出退出")
                xq = input("我:")
                if xq == '1' or xq == '简单':
                    jd = randint(1, 20)
                    while True:
                        try:
                            print("小安:请输入,它在1~20")
                            sh = int(input("我:"))
                            if sh == jd:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif sh < jd:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except BaseException:
                            print("小安:输入错误")
                elif xq == '2' or xq == '普通':
                    pt = randint(1, 50)
                    while True:
                        try:
                            print("小安:请输入,它在1~50")
                            shf = int(input("我:"))
                            if shf == pt:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shf < pt:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except BaseException:
                            print("小安:输入错误")
                elif xq == '3' or xq == '困难':
                    kn = randint(1, 100)
                    while True:
                        try:
                            shy = int(input("小安:请输入,它在1~100"))
                            if shy == kn:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shy < kn:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except BaseException:
                            print("小安:输入错误")
                elif xq == '4' or xq == '自定义':
                    print("小安:请输入范围,第一个数字和第二个数字用“，”隔开")
                    zdy, wwa = eval(input("我:"))
                    cszz = randint(zdy, wwa)
                    while True:
                        try:
                            print("小安:请输入,它在{}~{}".format(zdy, wwa))
                            shyq = int(input("我:"))
                            if shyq == cszz:
                                g += 1
                                print("小安:猜对了，猜了{}次".format(g))
                                g = 0
                                break
                            elif shyq < cszz:
                                g += 1
                                print("小安:小了")
                            else:
                                g += 1
                                print("小安:大了")
                        except BaseException:
                            print("小安:输入错误")
                elif xq == '5' or xq == '退出':
                    print("小安:退出猜数字")
                    break
                else:
                    print("小安:输入错误")
            except BaseException:
                print("小安:输入错误")
    elif y == '随机数':
        print("小安:请选择范围")
        print("小安:请输入第一个数字")
        mjs = int(input("我:"))
        print("小安:请输入第二个数字")
        mjs_2 = int(input("我:"))
        mjs_1 = randint(mjs, mjs_2)
        print("小安:本次{}~{}的随机数为{:2}".format(mjs, mjs_2, mjs_1))
    elif y == '奇数,偶数判断':
        while True:
            try:
                print("小安:请输入一个数字,输入字母退出")
                jo = eval(input("我:"))
                jo_1 = jo % 2
                if jo_1 == 0:
                    print("小安:这是一个偶数")
                else:
                    print("小安:这是一个奇数")
            except BaseException:
                print("小安:退出")
                break
    elif y == '中英文翻译':
        fy_1 = {'red': '红色'}
        while True:
            print("小安:请输入中文或英文,可输入“[录入]录入”,可输入“[删减]”删减，可输入“（退出）”退出")
            with open("fy_1.txt", 'r+') as f:  # 打开fy_1.txt文件
                line = f.read()
                fy_1 = eval(line)
            fy = input("我:")
            if fy in fy_1:
                fy_2 = fy_1["{}".format(fy)]
                print("小安:{}".format(fy_2))
            elif fy == '(退出)':
                print("小安:已退出")
                break
            elif fy == '[录入]':
                fy_3 = input("小安:请输入中文或英文")
                fy_4 = input("小安:请输入翻译")
                fy_1[fy_3] = fy_4
                with open("fy_1.txt", 'w') as f:
                    f.write(str(fy_1))
                print("小安:录入完毕")
            elif fy == '[删减]':
                print("小安:请输入需删减的内容")
                fy_5 = input("我:")
                del fy_1["{}".format(fy_5)]
                with open("fy_1.txt", "w") as f:
                    f.write(str(fy_1))
                print("小安:删减完毕")
            else:
                print("小安:请确认是否输入正确")
    elif y == '石头剪刀布':
        print("小安:石头为１，剪刀为２，布为３,记得只能输入数字哦\n输入45退出")
        print("小安:来吧")
        while True:
            try:
                jd = randint(1, 3)
                jd_1 = int(input("我:"))
                if jd == 1 and jd_1 == 1:
                    print("小安:我出的也是石头,嘻嘻")
                elif jd == 1 and jd_1 == 2:
                    print("小安:我出的是石头,我赢了")
                elif jd == 1 and jd_1 == 3:
                    print("小安:我出的是石头,emmm你赢了")
                elif jd == 2 and jd_1 == 1:
                    print("小安:我出的是剪刀,emmm你赢了")
                elif jd == 2 and jd_1 == 2:
                    print("小安:我出的也是剪刀,嘻嘻")
                elif jd == 2 and jd_1 == 3:
                    print("小安:我出的是剪刀,我赢了")
                elif jd == 3 and jd_1 == 1:
                    print("小安:我出的是布,我赢了")
                elif jd == 3 and jd_1 == 2:
                    print("小安:我出的是布,emmm你赢了")
                elif jd == 3 and jd_1 == 3:
                    print("我出的也是布,嘻嘻")
                elif jd_1 == 45:
                    print("小安:退出")
                    break
                else:
                    print("小安:出错了")
            except BaseException:
                print("小安:输入错误,请重新输入")
    elif y == '写字板':
        print("小安:请输入需要写的内容")
        xzb = input("我:")
        print("小安:请输入字体大小")
        xzb_1 = input("我:")
        print("小安:请输入字体颜色,仅限英文")
        xzb_2 = input("我:")
        cc()
        pencolor(xzb_2)
        write(xzb, font=("Arial", xzb_1, "normal"))
    elif y == '写文件':
        print("小安:请输入需要写入的内容")
        xwj = input("我:")
        print("请输入需要保存的文件名,需包含文件的后缀名")
        xwj_1 = input("我:")
        xwj_2 = open(xwj_1, "w+")
        xwj_2.write(xwj)
        for line in xwj_2:
            print(line)
        xwj_2.close()
    elif y == '速算':
        fs = 0
        now = datetime.now()
        while True:
            print("小安:请选择难度\n1.简单\t2.困难\n输入'666'退出")
            x1 = input("我:")
            if x1 == '1' or x1 == '简单':
                while True:
                    jd = randint(0, 10)
                    jd_1 = randint(0, 10)
                    jd_2 = randint(1, 2)
                    if jd_2 == 1:
                        print("小安:{}+{}=".format(jd, jd_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        jd_4 = int(input("我:"))
                        jd_3 = jd + jd_1
                        if jd_3 == jd_4:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif jd_4 == 999:
                            print("小安:退出简单模式")
                            break
                        elif jd_4 == 333:
                            zc = open("zc.txt", "a+")
                            zc_1 = ["难度:简单 分数:{:2}\t保存时间:{}\n".format(fs, now)]
                            zc.writelines(zc_1)
                            for line in zc:
                                print(line)
                                zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
                    else:
                        print("小安:{}-{}=".format(jd, jd_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        jd_5 = int(input("我:"))
                        jd_6 = jd - jd_1
                        if jd_5 == jd_6:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif jd_5 == 999:
                            print("小安:退出简单模式")
                            break
                        elif jd_5 == 333:
                            zc = open("zc.txt", "a+")
                            zc_1 = ["难度:简单 分数:{:2}\t保存时间:{}\n".format(fs, now)]
                            zc.writelines(zc_1)
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
            elif x1 == '2' or x1 == '困难':
                while True:
                    kn = randint(10, 20)
                    kn_1 = randint(10, 20)
                    kn_2 = randint(1, 2)
                    if kn_2 == 1:
                        print("小安:{}+{}=".format(kn, kn_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        kn_3 = int(input("我:"))
                        if kn_3 == kn + kn_1:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif kn_3 == 999:
                            print("小安:退出困难模式")
                            break
                        elif kn_3 == 333:
                            zc = open("zc.txt", "a+")
                            zc.write(
                                "难度:困难 分数:{:2}\t保存时间:{}\n".format(
                                    fs, now))
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("小安:当前分数:{}".format(fs))
                    else:
                        print("小安:{}-{}=".format(kn, kn_1))
                        print("小安:输入'999'退出,输入'333'保存")
                        kn_5 = int(input("我:"))
                        kn_6 = kn - kn_1
                        if kn_5 == kn_6:
                            print("小安:回答正确")
                            fs += 1
                            print("小安:当前分数:{}".format(fs))
                        elif kn_5 == 999:
                            print("小安:退出困难模式")
                            break
                        elif kn_5 == 333:
                            zc = open("zc.txt", "a+")
                            zc.write(
                                "难度:困难 分数:{:2}\t保存时间:{}\n".format(
                                    fs, now))
                            for line in zc:
                                print(line)
                            zc.close()
                            print("小安:保存完毕")
                            fs = 0
                        else:
                            print("小安:回答错误")
                            fs -= 1
                            print("当前分数:{}".format(fs))
            elif x1 == '666' or x1 == '６６６':
                print("小安:退出")
                break
            else:
                print("小安:输入错误")
    elif y == '天气查询':
        while True:
            try:
                print("小安:请输入查询的城市(输入“退出”退出):")
                str1 = input("我:")
                if str1 == '退出':
                    print("小安:退出天气查询")
                    break
                url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + str1
                response = requests.get(url)
                wearher_json = json.loads(response.text)
                a = wearher_json['data']
                print("当前位置：" + a['city'])
                print("温馨提示：" + a['ganmao'])
                print("当前温度：" + a['wendu'] + '℃')
                print("昨天：" + a['yesterday']['date'])
                print("风力：" + a['yesterday']['fl'][9:[m.start()
                                                      for m in re.finditer(']', a['yesterday']['fl'])][0]])
                print("风向：" + a['yesterday']['fx'])
                print(a['yesterday']['high'])
                print(a['yesterday']['low'])
                print("天气：" + a['yesterday']['type'])
                print("--------------------------------")
                for i in range(0, 4):
                    print("时间：" + a["forecast"][i]['date'])
                    print('风力: ' + a["forecast"][i]['fengli'][9:[m.start()
                                                                 for m in re.finditer(']', a['yesterday']['fl'])][0]])
                    print('风向：' + a["forecast"][i]['fengxiang'])
                    print(a["forecast"][i]['high'])
                    print(a["forecast"][i]['low'])
                    print("天气：" + a["forecast"][i]['type'])
                    print("--------------------------------")
            except BaseException:
                print("小安:天气查询失败,请检查网络是否连接,或者请查看是否输入错误")
    elif y == '画板':
        while True:
            print("小安:请输入画笔大小,输入help查看功能")
            hbaz = input("我:")
            if hbaz == 'help':
                print(
                    "小安:1.向右\n2.向左\n3.向前\n4.抬笔\n5.落笔\n6.清空\n7.画笔颜色\n8.到达坐标\n9.画圆\n10.背景颜色\n11.角度")
            else:
                pensize(int(hbaz))
                break
        while True:
            print("小安:请输入画笔的运动,输入“退出”退出")
            hb = input("我:")
            if hb == '向右':
                print("小安:请输入移动像素")
                hby = int(input("我:"))
                right(hby)
            elif hb == '向左':
                print("小安:请输入移动像素")
                hbz = int(input("我:"))
                left(hbz)
            elif hb == '向前':
                print("小安:请输入移动像素")
                hbq = int(input("我:"))
                fd(hbq)
            elif hb == '抬笔':
                penup()
            elif hb == '落笔':
                pendown()
            elif hb == '清空':
                cc()
            elif hb == '画笔颜色':
                print("小安:请输入画笔颜色,仅限英文\n如:red(红色),green(绿色),black(黑色),yellow(黄色),white(白色),grey(灰色),darkgreen(深绿色),gold(金色),violet(紫罗兰),purple(紫色)")
                hbys = input("我:")
                pencolor(hbys)
            elif hb == '退出':
                print("小安:退出")
                break
            elif hb == '到达坐标':
                print("小安:请输入第一个数字")
                hbzb = int(input("我:"))
                print("小安:请输入第二个数字")
                hbzb_2 = int(input("我:"))
                goto(hbzb, hbzb_2)
            elif x == '画圆':
                print("小安:请输入圆的半径")
                hbyuan = input("我:")
                circle(int(hbyuan))
            elif x == '背景颜色':
                windowe = Screen()
                print("小安:请输入背景颜色,仅限英文\n如:red(红色),green(绿色),black(黑色),yellow(黄色),white(白色),grey(灰色),darkgreen(深绿色),gold(金色),violet(紫罗兰),purple(紫色)")
                hbbj = input("我:")
                windowe.bgcolor(hbbj)
            elif hb == '角度':
                hbjd = int(input())
                seth(hbjd)
            else:
                print("输入错误")
    elif '+' and '=' in y or '-' and '=' in y or '+' and '-' and '=' in y or '*' and '=' in y:
        print("小安:你是要计算吗?你可已输入“计算机”进行计算")
    elif y == '翻译':
        try:
            while True:
                print("小安:请输入中文或英文(仅限英文和中文),输入“[退出]”退出")
                d = input('我:')
                if d == '[退出]':
                    print("小安:退出翻译")
                    break
                heads = {}
                heads['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'

                now = datetime.now()
                now = now.timestamp()

                a = re.match(r'(\d+)\.(\d+)', str(now))
                b = a.group(1) + a.group(2)
                f = b[:13]  # 时间戳前13位

                c = "rY0D^0'nM0}g5Mm1z%1G4"
                u = 'fanyideskweb'

                creatmd5 = u + d + f + c

                # 生成md5
                md5 = hashlib.md5()
                md5.update(creatmd5.encode('utf-8'))
                sign = md5.hexdigest()

                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='

                data = {}
                data['i'] = d
                data['from'] = 'AUTO'
                data['to'] = 'AUTO'
                data['smartresult'] = 'dict'
                data['client'] = 'fanyideskweb'
                data['salt'] = f
                data['sign'] = sign
                data['doctype'] = 'json'
                data['version'] = '2.1'
                data['keyfrom'] = 'fanyi.web'
                data['action'] = 'FY_BY_CLICKBUTTION'
                data['typoResult'] = 'true'

                data = urllib.parse.urlencode(data).encode('utf-8')

                req = urllib.request.Request(
                    url=url, data=data, method='POST', headers=heads)
                # 想要使用动态追加头headers，必须使Request类实例化，对象有动态追加函数req.add_headers()的方法
                response = urllib.request.urlopen(req)

                translateResult = response.read().decode('utf-8')

                target = json.loads(translateResult)

                print(target['translateResult'][0][0]['tgt'])
        except BaseException:
            print("小安:翻译失败，请检查网络是否连接")
            print("小安:退出翻译")
    elif y == '智能对话':
        info = 'w'
        for i in range(10):
            if info == '[退出]':
                break
            print("小安:如果没有ID和密码,请在ID输入“YH-ZJ”,请在密码输入“1001”(登录这个ID需要一个图灵机器人)")
            print("小安:请输入ID")
            ID = input("我:")
            print("小安:请输入密码")
            MM = input("我:")
            if ID == 'CYG-GLY' and MM == '12131':
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        # 将得到的 json 格式的信息转换为 Python 的字典格式
                        data = json.loads(res.text)
                        print('小安:' + data['text'])  # 输出结果
                except BaseException:
                    print("对话失败,请确认网络是否连接")
            elif ID == 'YH-KK' and MM == '0100':
                key_TY = 'b7e054da696f40d8b026a40435c0a7e4'
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + \
                            key_TY + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        # 将得到的 json 格式的信息转换为 Python 的字典格式
                        data = json.loads(res.text)
                        print('小安:' + data['text'])  # 输出结果
                except BaseException:
                    print("对话失败,请确认网络是否连接")
            elif ID == 'YH-ZJ' and MM == '1001':
                print("小安:请输入图灵aip")
                key_YH = input("我:")
                print("小安:现在你能和我对话了哟,不过记得先连网,如过不想和我对话了可以输入“[退出]”")
                try:
                    while True:
                        info = input('我:')  # 输入对话信息
                        if info == '[退出]':
                            print("小安:退出")
                            break
                        url = 'http://www.tuling123.com/openapi/api?key=' + \
                            key_YH + '&info=' + info  # 拼接 url
                        res = requests.get(url)  # 得到数据
                        res.encoding = 'utf-8'  # 防止中文乱码
                        # 将得到的 json 格式的信息转换为 Python 的字典格式
                        data = json.loads(res.text)
                        print('小安:' + data['text'])  # 输出结果
                except BaseException:
                    print("对话失败,请确认网络是否连接")

            else:
                print("小安:密码或ID错误")
                CW = 9 - i
                print("小安:你还有{}次机会".format(CW))
                if CW == 0:
                    print("小安:退出智能对话")
                    break
    elif y == '温度转换':
        print("请输入带有符号的温度值:")
        wd = input("我:")
        if wd[-1] in ['F', 'f']:
            C = (eval(wd[0:-1]) - 32) / 1.8
            print("小安:转换后的温度是{:.2f}C".format(C))
        elif wd[-1] in ['C', 'c']:
            F = 1.8 * eval(wd[0:-1]) + 32
            print("小安:转换后的温度是{:.2f}F".format(F))
        else:
            print("小安:输入格式错误")
    elif y == '打开百度':
        os.rename(r'df\q.dll', r'df\q.html')
        os.system(r"df\q.html")
        sleep(1)
        os.rename(r'df\q.html', r'df\q.dll')
    elif y == '打开浏览器':
        os.rename(r'df\sd.dll', r'df\sd.html')
        os.system(r"df\sd.html")
        sleep(1)
        os.rename(r'df\sd.html', r'df\sd.dll')
    elif y == '特效':
        while True:
            print("小安:请选择特效(输入“[退出]”退出)\n1.烟花 2.粒子风暴 3.鼠标 4.代码流")
            tx = input("我:")
            if tx == '1' or tx == '烟花':
                os.rename(r'df\zx.dll', r'df\zx.html')
                os.system(r"df\zx.html")
                sleep(1)
                os.rename(r'df\zx.html', r'df\zx.dll')
            elif tx == '2' or tx == '粒子风暴':
                os.rename(r'df\qq.dll', r'df\qq.html')
                os.system(r"df\qq.html")
                sleep(1)
                os.rename(r'df\qq.html', r'df\qq.dll')
            elif tx == '3' or tx == '鼠标':
                os.rename(r'df\sb.dll', r'df\sb.html')
                os.system(r"df\sb.html")
                sleep(1)
                os.rename(r'df\sb.html', r'df\sb.dll')
            elif tx == '4' or tx == '代码流':
                os.rename(r'df\dml.dll', r'df\dml.html')
                os.system(r"df\dml.html")
                sleep(1)
                os.rename(r'df\dml.html', r'df\dml.dll')
            elif tx == '[退出]':
                print("小安:退出特效")
                break
            else:
                print("小安:输入错误")
    elif y == '时钟':
        os.rename(r'df\sj.dll', r'df\sj.html')
        os.system(r"df\sj.html")
        sleep(1)
        os.rename(r'df\sj.html', r'df\sj.dll')
    elif y == '播放音乐':
        while True:
            song_1 = input("小安:请输入歌曲名(输入“[退出]”退出)")
            song_2 = os.listdir(r'df\缓存歌曲')
            song_3 = '{}.mp3'.format(song_1)
            if song_1 == '[退出]':
                print("小安:退出")
                break
            if song_3 not in song_2:
                try:
                    song = get_songs_info(song_1)
                except BaseException:
                    print("小安:播放错误,请在缓存歌曲文件夹里看看缓存歌曲是否有问题")
                dow_song(song['song_id'], song['song_name'])
            yy_1 = int(input("小安:请输入播放次数\n我:"))
            yy_2 = int(input("小安:请输入播放的时间,输入“０”播放整首\n我:"))
            if yy_2 == 0:
                for i in range(yy_1):
                    print("小安:播放中...")
                    playsound(r'df\缓存歌曲\{}.mp3'.format(song_1))
                    print("播放结束")
            elif yy_2 > 0:
                for i in range(yy_1):
                    file = r'df\缓存歌曲\{}.mp3'.format(song_1)
                    pygame.mixer.init()
                    print("播放中...")
                    track = pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    sleep(yy_2)
                    pygame.mixer.music.stop()
                    print("小安:播放结束")
            else:
                print("小安:输入错误")
    elif y == '加密解密':
        while True:
            jmjm = input("小安:请选择加密或解密方式1.凯撒秘密码 2.摩斯密码 3.其他 4.退出\n我:")
            if jmjm == '1' or jmjm == '凯撒密码':
                ks = input("\n小安:请输入\n1.加密 2.解密 \n我:")
                if ks == '1' or ks == '加密':
                    jm = input("\n小安:请输入需加密的内容\n我:")
                    try:
                        jm_1 = int(input("\n小安:请输入密匙\n我:"))
                    except BaseException:
                        print("小安:密匙输入错误,密匙必须是数字")
                    print("小安:加密结果是\n")
                    for p in jm:
                        if ord("a") <= ord("p") <= ord("z"):
                            jmjg = chr(
                                ord("a") + (ord(p) - ord("a") + jm_1) % 26)
                            print("{}".format(jmjg), end='')
                        else:
                            print("{}".format(p))
                elif ks == '2' or ks == '解密':
                    jm_3 = input("\n小安:请输入需解密的内容\n我:")
                    try:
                        jm_4 = int(input("\n小安:请输入密匙\n我:"))
                    except BaseException:
                        print("小安:密匙输入错误,密匙必须是数字")
                    print("小安:解密结果是\n")
                    for p in jm_3:
                        if ord("a") <= ord("p") <= ord("z"):
                            jmjg_1 = chr(
                                ord("a") + (ord(p) - ord("a") - jm_4) % 26)
                            print("{}".format(jmjg_1), end='')
                        else:
                            print("{}".format(p), end='')
                else:
                    print("小安:输入错误")
            elif jmjm == '2' or jmjm == '摩斯密码':
                msmm = {
                    'A': '.-',
                    'a': '.- ',
                    'B': '-...',
                    'b': '-... ',
                    'C': '-.-.',
                    'c': '-.-. ',
                    'D': '-..',
                    'd': '-.. ',
                    'E': '.',
                    'e': '. ',
                    'F': '..-.',
                    'f': '..-. ',
                    'G': '--.',
                    'g': '--.',
                    'H': '....',
                    'h': '.... ',
                    'I': '..',
                    'i': '.. ',
                    'J': '.---',
                    'j': '.--- ',
                    'K': '-.-',
                    'k': '-.- ',
                    'L': '.-..',
                    'l': '.-.. ',
                    'M': '--',
                    'm': '-- ',
                    'N': '-.',
                    'n': '-. ',
                    'O': '---',
                    'o': '--- ',
                    'P': '.--.',
                    'p': '.--. ',
                    'Q': '--.-',
                    'q': '--.- ',
                    'R': '.-.',
                    'r': '.-. ',
                    'S': '...',
                    's': '... ',
                    'T': '-',
                    't': '- ',
                    'U': '..-',
                    'u': '..- ',
                    'V': '...- ',
                    'v': '...- ',
                    'W': '.--',
                    'w': '.-- ',
                    'X': '-..-',
                    'x': '-..- ',
                    'Y': '-.--',
                    'y': '-.-- ',
                    'Z': '--..',
                    'z': '--.. ',
                    '1': '.---- ',
                    '2': '..--- ',
                    '3': '...-- ',
                    '4': '....- ',
                    '5': '..... ',
                    '6': '-.... ',
                    '7': '--... ',
                    '8': '---.. ',
                    '9': '----. ',
                    '0': '----- ',
                    '?': '..--.. ',
                    '/': '-..-. ',
                    '(': '-.--.- ',
                    ')': '-.--.- ',
                    '-': '-....- ',
                    '.': '.-.-.- '}
                while True:
                    msmm_3 = input("小安: 1.加密 2.解密 3.退出")
                    if msmm_3 == '1' or msmm_3 == '加密':
                        msmm_1 = input("小安:请输入英文(输入'退出'退出)\n我:")
                        if msmm_1 == '退出':
                            print("小安:退出")
                            break
                        print("小安:", end='')
                        for msmm_1 in msmm_1:
                            if msmm_1 not in msmm:
                                print("{:2}".format(msmm_1), end='')
                            else:
                                msmm_2 = msmm["{}".format(msmm_1)]
                                print("  {:4}".format(msmm_2), end="")
                                sleep(0.05)
                        print(" ")
                    elif msmm_3 == '2' or msmm_3 == '解密':
                        msmmjm = ''
                        while True:
                            try:
                                msmm_jm = input(
                                    "小安:请输入每输完一个就要加一个空格,输入‘退出’退出\n我:")
                                if '退出' in msmm_jm:
                                    break
                                for msmm_jm in msmm_jm:
                                    msmmjm += msmm_jm
                                    if ' ' in msmmjm:
                                        di = {v: k for k, v in msmm.items()}
                                        q = di[msmmjm]
                                        print('{}'.format(q), end='')
                                        msmmjm = ''
                                print('')
                            except BaseException:
                                print("小安:输入错误")
                    elif msmm_3 == '3' or msmm_3 == '退出':
                        break
            elif jmjm == '3' or jmjm == '其他':
                qt = input("小安:请选择1.加密 2.解密\n我:")
                if qt == '1' or qt == '加密':
                    qtjm = input("小安:请输入需加密的内容\n我:")
                    try:
                        qtjm_1 = int(input("小安:请输入密匙\n我:"))
                    except BaseException:
                        print("小安:输入错误")
                    for qtjm in qtjm:
                        qtjm_2 = ord(qtjm)
                        qtjm_2 += qtjm_1
                        qtjm_3 = chr(qtjm_2)
                        print("{}".format(qtjm_3), end='')
                        sleep(0.05)
                    print(" ")
                elif qt == '2' or qt == '解密':
                    qtjm_0 = input("小安:请输入需解密的内容\n我:")
                    try:
                        qtjm_4 = int(input("小安:请输入密匙\n我:"))
                    except BaseException:
                        print("小安:输入错误")
                    for qtjm_0 in qtjm_0:
                        qtjm_5 = ord(qtjm_0)
                        qtjm_5 -= qtjm_4
                        qtjm_7 = chr(qtjm_5)
                        print("{}".format(qtjm_7), end='')
                        sleep(0.05)
                    print(" ")
                else:
                    print("小安:输入错误")
            elif jmjm == '4' or jmjm == '退出':
                print("小安:退出")
                break
    elif y == '数量计算':
        sl = 0
        while True:
            sljs = input("小安:请选择\n1.计算单个字或词，句子 2.计算全部 3.文件字数计算 4.退出\n我:")
            if sljs == '1' or sljs == '计算单个字或词句子':
                dgz = input("小安:请输入内容\n我:")
                dgz_1 = input("小安:请输入需计算的单个字或词，句子\n我:")
                dgz_3 = dgz.count(dgz_1)
                print("小安:有{}个".format(dgz_3))
                sl = 0
            elif sljs == '2' or sljs == '计算全部':
                qb = input("小安:请输入内容\n我:")
                for qb in qb:
                    if ' ' in qb:
                        sl -= 1
                    elif sl < 1:
                        sl = 0
                    sl += 1
                print("小安:有{}个".format(sl))
                sl = 0
            elif sljs == '4' or sljs == '退出':
                print("小安:退出")
                break
            elif sljs == '3' or sljs == '文件字数计算':
                while True:
                    wjsz = input("小安:请选择 1.计算全部 2.计算单个字或词，句子 3.退出\n我:")
                    if wjsz == '1' or wjsz == '计算全部':
                        try:
                            wjjs = input("小安请输入，需包括文件名\n我：")
                            wj = open(wjjs, 'r').read()
                            for wj in wj:
                                sl += 1
                                if ' ' in wj:
                                    sl -= 1
                                elif '\n' in wj:
                                    sl -= 1
                                elif sl < 1:
                                    sl = 0
                            print("小安:有{}个".format(sl))
                            sl = 0
                            break
                        except FileNotFoundError:
                            print("小安:找不到此文件")
                    elif wjsz == '2' or wjsz == '计算单个字或词，句子':
                        try:
                            dg = input("小安请输入，需包括文件名\n我：")
                            dg_1 = open(dg, 'r').read()
                            dg_2 = input("小安:请输入需计算的单个字或词，句子\n我:")
                            for dg_1 in dg_1:
                                if dg_2 in dg_1:
                                    sl += 1
                            print("小安:有{}个".format(sl))
                            sl = 0
                            break
                        except FileNotFoundError:
                            print("小安:找不到文件")
                    elif wjsz == '3' or wjsz == '退出':
                        print("小安:退出")
                        break
                    else:
                        print("小安:输入错误")
            else:
                print("小安:输入错误,请重新输入")
    elif y == '运气测试':
        wqcs = datetime.now()
        wqcs_1 = wqcs.strftime("%Y%m%d")
        with open("df/sjs.dll", 'r+') as f:
            lineq = f.read()
        wqcs_4 = int(wqcs_1)
        wqcs_5 = int(lineq)
        wqcs_3 = wqcs_4 - wqcs_5
        if wqcs_3 == 0:
            print("小安:你今天的次数已用完,请明天再来")
        else:
            print("小安:欢迎进入")
            sls = 1
            try:
                yc = int(input("小安:请输入一个数字,需在1~20之间\n我:"))
            except BaseException:
                print("小安:请输入数字")
            while True:
                yc_2 = randint(1, 20)
                if yc < 0 or yc > 20:
                    print("小安:输入错误")
                    break
                if yc != yc_2:
                    sls += 1
                else:
                    print("小安:你所输入的数字用了{}次中了".format(sls))
                    if sls < 20:
                        print("小安:你本次的运气贼好")
                    elif 21 > sls < 50:
                        print("小安:你本次的运气一般")
                    else:
                        print("小安:你本次的运气不够好")
                        sls = 1
                    cssj = datetime.now()
                    cssj_2 = cssj.strftime("%Y%m%d")
                    cssj_3 = open("df/sjs.dll", "w+")
                    cssj_3.write(cssj_2)
                    cssj_3.close()
                    break
    elif y == '二元一次方程计算':
        print("小安:二元一次方程组请采用如下格式输入：ax+by=e，cx+dy=f，\n如果任何一个方程中有x或者y不存在，请用0x或者0y补齐,输入”退出“退出")
        while True:
            equa = input("小安:请输入二元一次方程组，方程之间用英文逗号隔开\n我:")
            if equa == '退出':
                print("小安:退出")
                break
            d = main(equa)
            print("小安:该二元一次方程组的解为:x={0[0]:}，y={0[1]:}".format(d))
            d = input()
            if d != "":
                exit()
    elif y == '简单计算':
        root = Tk()  # 给窗体
        root.title('calculator')  # 设置窗体名字
        frm = Frame(root, bg='pink')  # 新建框架
        frm.pack(expand=YES, fill=BOTH)  # 放置框架
        display = StringVar()
        e = Entry(frm, textvariable=display)  # 添加输入框
        e.grid(row=0, column=0, sticky=N, columnspan=4, rowspan=2)  # 放置输入框位置

        def print_jia():
            e.insert(INSERT, '+')

        def print_jian():
            e.insert(INSERT, '-')

        def print_cheng():
            e.insert(INSERT, '*')

        def print_chu():
            e.insert(INSERT, '/')

        def print_dengyu():
            e.insert(INSERT, '=')

        def cal(display):
            try:
                display.set(eval(display.get()))
            except Exception as e:
                display.set(e)

        Button(
            frm,
            text='1',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '1')).grid(
            row=2,
            column=0,
            sticky=W)  # 设置按钮，lambda为匿名函数
        Button(
            frm,
            text='2',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '2')).grid(
            row=2,
            column=1)
        Button(
            frm,
            text='3',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '3')).grid(
            row=2,
            column=2)
        Button(
            frm,
            text='4',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '4')).grid(
            row=3,
            column=0,
            sticky=W)
        Button(
            frm,
            text='5',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '5')).grid(
            row=3,
            column=1)
        Button(
            frm,
            text='6',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '6')).grid(
            row=3,
            column=2)
        Button(
            frm,
            text='7',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '7')).grid(
            row=4,
            column=0,
            sticky=W,
            rowspan=2)
        Button(
            frm,
            text='8',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '8')).grid(
            row=4,
            column=1,
            rowspan=2)
        Button(
            frm,
            text='9',
            width=3,
            bg='yellow',
            command=lambda: e.insert(
                INSERT,
                '9')).grid(
            row=4,
            column=2,
            rowspan=2)
        Button(
            frm,
            text='/',
            width=4,
            bg='white',
            command=print_chu).grid(
            row=5,
            column=3,
            sticky=E)
        Button(
            frm,
            text='*',
            width=4,
            bg='white',
            command=print_cheng).grid(
            row=4,
            column=3,
            sticky=E)
        Button(
            frm,
            text='-',
            width=4,
            bg='white',
            command=print_jian).grid(
            row=3,
            column=3,
            sticky=E)
        Button(
            frm,
            text='+',
            width=4,
            bg='white',
            command=print_jia).grid(
            row=2,
            column=3,
            sticky=E)
        Button(
            frm,
            text='=',
            width=4,
            bg='white',
            command=lambda: cal(display)).grid(
            row=6,
            column=3,
            sticky=E)
        Button(
            frm,
            text='clear',
            width=3,
            bg='red',
            command=lambda: display.set('')).grid(
            row=6,
            column=0,
            sticky=W)
        Button(
            frm,
            text='0',
            width=3,
            bg='red',
            command=lambda: e.insert(
                INSERT,
                '0')).grid(
            row=6,
            column=2)
        Button(
            frm,
            text='.',
            width=3,
            bg='red',
            command=lambda: e.insert(
                INSERT,
                '.')).grid(
            row=6,
            column=1)

        root.mainloop()  # 让程序一直循环
    elif y == '闹钟':
        os.rename(r'df\znz.dll', r'df\znz.exe')
        os.system(r"df\znz.exe")
        try:
            sleep(1)
            os.rename(r'df\znz.exe', r'df\znz.dll')
        except BaseException:
            print("")
    elif y == '复制文字':
        while True:
            fzwz = input(
                "小安:请选择 1.复制在一行,如下:asasasas 2.每个一行,如下:\nas\nas\nas \n3.退出(内容和次数输入0)\n我:")
            fzny = input("小安:请输入需复制的内容\n我:")
            try:
                fzcs = int(input("小安:请输入需复制的次数\n我:"))
            except BaseException:
                print("小安:输入错误")
            if fzwz == '1' or fzwz == '复制在一行':
                fzcs_2 = fzny * fzcs
                wjj = open("复制内容.txt", "w+")
                wjj.write(fzcs_2)
                wjj.close()
                print("小安:复制完毕，在复制内容.txt里")
            elif fzwz == '2' or fzwz == '每个一行':
                fzcs_1 = ("{}\n".format(fzny))
                fzcs_3 = fzcs_1 * fzcs
                wjj = open("复制内容.txt", "w+")
                wjj.write(fzcs_3)
                wjj.close()
                print("小安:复制完毕，在复制内容.txt里")
            elif fzwz == '3' or fzwz == '退出':
                print("小安:退出")
                break
            else:
                print("小安:输入错误")
    else:
        print("小安:emmm,我无法回答")  # 机器人学习
        print("小安:是否需要我学习?")
        s = input("我:")
        while True:
            if '是' in s:
                s_1 = input("小安:请输入你的问题")
                s_2 = input("小安:请输入你的希望得到的回答")
                x[s_1] = s_2
                print("小安:已学习完毕")
                with open("df/nc.txt", 'w') as f:
                    f.write(str(x))
                break
            elif '否' in s or '不' in s:
                print("小安:那好吧")
                break
            else:
                print("小安:请回答我的问题,是否需要我学习")
                s = input("我:")
