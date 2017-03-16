from pandas import DataFrame, Series
import numpy as np

series = Series(np.arange(3))
print(series)
# 0    0
# 1    1
# 2    2
# dtype: int32
print(series[0])
# 0
# print(series[-1])
# 这里会抛出异常

# 如果是非整数索引，那么使用-1就不会抛出异常
series2 = Series(np.arange(3), index=['a', 'b', 'c'])
print(series2[-1])
# 2

# 原因就是，系统不知道用户希望按照标签（实际存在的0,1,2） 还是按照位置（第一个是0，第二个是1）
# 使用ix总是面向标签的

print(series.ix[:1])
# 0    0
# 1    1
# dtype: int32

# 使用Series的iloc[i]/iat[i]和DataFrame的iloc[i]/iloc[:,i]总是面向位置的

series3 = Series(range(3), index=[-5, 1, 3])
print(series3)
# -5    0
#  1    1
#  3    2
# dtype: int32
print(series3.iat[2])
# 2
print(series3.iloc[2])
# 2

frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
print(frame)
#    0  1
# 2  0  1
# 0  2  3
# 1  4  5

# 第0行
print(frame.iloc[0])
# 0    0
# 1    1

# 第0列
print(frame.iloc[:, 0])
# 2    0
# 0    2
# 1    4
# Name: 0, dtype: int32

