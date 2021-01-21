"""
    Pandas简单操作
"""
import pandas as pd
import numpy as np

# DataFrame
# 生成数据
data_1 = np.random.normal(0, 1, (10, 5))

# 生成列索引
data_3 = ["股票{}".format(i) for i in range(10)]

# 生成行索引
date = pd.date_range(start='2020-01-01', periods=5, freq="B")

# 设置索引
data_2 = pd.DataFrame(data_1, index=data_3, columns=date)

# 修改索引
data_4 = ["股票__{}".format(i) for i in range(10)]
data_2.index = data_4

# # 重设索引
# data_5 = data_2.reset_index(drop=False)
# 
# print(data_5)


# # Series
# # 数据的产生
# data_6 = pd.Series(np.arange(10))
#
# print(data_6)


# 运算
# data_5 = data_2["2020-01-01"] + 3
data_5 = data_2["2020-01-01"].add(3).head()

print(data_5)
