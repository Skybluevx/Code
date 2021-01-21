"""
    使用 matplotlib 绘制简单的图形
"""
import matplotlib.pyplot as plt
import random


# 显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 显示负号
plt.rcParams["axes.unicode_minus"] = False

# 绘制折线图

# 创建数据
time = range(60)
t_shanghai = [random.uniform(15, 18) for i in time]
t_beijing = [random.uniform(1, 3) for z in time]

# # 创建画布
# plt.figure(figsize=(20, 8), dpi=200)
#
# # 绘制图形
# plt.plot(time, t_shanghai, color="red", linestyle=":", label="上海")
# plt.plot(time, t_beijing, color="blue", linestyle="-.", label="北京")
#
# # 显示图例
# plt.legend()
#
# # 修改 x，y 坐标
# time_h = [u"11点{}分".format(i) for i in time]
# plt.xticks(time[::5], time_h[::5])
# plt.yticks(range(0, 36, 5))
#
# # 增加x，y轴的标题
# plt.xlabel("时间")
# plt.ylabel("温度")
#
# # 增加表格标题
# plt.title("中午11点到12点温度变化图示")
#
# # 增加网格
# plt.grid(True, linestyle="--", alpha=0.5)
#
# # 显示图像
# plt.show()
#
# # 绘制散点图
# plt.figure()
# plt.scatter(time, t_beijing)
# plt.show()

# 绘制柱状图（一）
# plt.figure(figsize=(20, 8), dpi=200)
# plt.bar(range(len(time)), t_beijing, color="r")
# plt.xticks(range(len(time)), range(60, 120))
# plt.show()

# # 绘制柱状图（二）
# # 1.准备数据
# movie_name = ["雷神3", "正义联盟", "寻梦环游记"]
# first_day = [10587.6, 10062.5, 1275.7]
# first_weekend = [36224.9, 34479.6, 11830]
# x = range(len(movie_name))
#
# # 2.创建画布
# plt.figure(figsize = (20, 8), dpi=100)
#
# # 3.绘制图像
# plt.bar([i - 0.1 for i in x], first_day, width=0.2, color="r")
# plt.bar([i + 0.1 for i in x], first_weekend, width=0.2, color="b")
#
# plt.xticks(x, movie_name)
# # 展示图像
# plt.show()
#

# # 绘制直方图
# # 1.数据准备
# distance = 2
# x = []
# group_num = (max(x) - min(x)) // distance
#
# # 2.创建画布
# plt.figure(figsize=(20, 8), dpi=100)
#
# # 3.绘制图像
# plt.hist(x, bins=distance)
#
# # 4.展示图像
# plt.show()
