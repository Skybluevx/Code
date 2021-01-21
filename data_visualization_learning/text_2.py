"""
    Numpy的简单操作
"""
import numpy as np
import matplotlib.pyplot as plt


# score = np.array([[80, 89, 86, 67, 79],
#                   [78, 97, 89, 67, 81],
#                   [90, 94, 78, 67, 74],
#                   [91, 91, 90, 67, 69],
#                   [76, 87, 75, 67, 86],
#                   [70, 79, 84, 67, 84],
#                   [94, 92, 93, 67, 64],
#                   [86, 85, 83, 67, 80]])


# 生成0和1的数组
# data_1 = np.zeros(shape=(3, 4), dtype="float32")
# data_2 = np.ones(shape=(4, 3))


# 从现有的数组生成
# 深拷贝
# data_3 = np.array(score)
# data_5 = np.copy(score)
# 浅拷贝
# data_4 = np.asarray(score)


# 生成固定范围的数组
# data_6 = np.linspace(0, 10, 100)  # 等距离，0到10，100个
# data_7 = np.arange(0, 10, 2)  # 0到10，步长2


# 生成随机数组
# data_8 = np.random.rand()
# data_9 = np.random.uniform(low=-1, high=1, size=1000000)  # 最常用
# data_10 = np.random.randint()

# 正态分布
# data_11 = np.random.randn()
# data_12 = np.random.normal(loc=1.75, scale=0.1, size=1000000)  # 最常用
# data = np.random.standard_normal()

# plt.figure(figsize=(20, 8), dpi=100)
# plt.hist(data_12, bins=1000)
# plt.show()
#
# print(data_12)

"""
    案例：随机生成8只股票2周的交易日涨幅数据。
"""
# 数据生成
stock_change = np.random.normal(loc=0, scale=1, size=(8, 10))

# 获取第一个股票的前3个交易日的涨幅数据
# data_13 = stock_change[0, :3]


# 形状修改
# data_14 = stock_change.reshape(80, 1)  # 改变为指定的性状的数组（只修改形状）
# stock_change.resize((10, 8))  # 没有返回值，对原始的数据进行修改
# data_15 = stock_change.T  # 行列数据转换


# 逻辑运算
data_16 = stock_change > 0.5
data_17 = stock_change[data_16]  # bool 索引，可对数组内满足条件的数据进行操作

print(data_17)

