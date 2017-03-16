from pandas import DataFrame, Series
import numpy as np

# 层次化索引：在一个轴上拥有多个索引级别
# index由一个数组/列表组成的列表组成
data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
# a  1   -0.068191
#    2    0.452962
#    3    0.749466
# b  1    0.827239
#    2   -0.127824
#    3   -0.853068
# c  1   -0.441021
#    2    0.791153
# d  2   -0.861513
#    3    0.192695
# dtype: float64

print(data.index)
# MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3]],
#            labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
# 选取一个数据子集
print(data['b'])
# 1    0.347276
# 2   -1.712556
# 3   -0.488840
# dtype: float64


# 在下标中使用切片，或者ix方法
print(data['b':'c'])
# b  1    2.818543
#    2   -0.930246
#    3   -0.288924
# c  1    0.100251
#    2   -0.409984
# dtype: float64
print(data.ix[['b', 'd']])
# b  1    2.818543
#    2   -0.930246
#    3   -0.288924
# d  2   -0.056511
#    3   -0.321154
# dtype: float64

# 在内层中进行选取
print(data[:, 2])
# a    0.046415
# b    0.581287
# c   -0.203951
# d   -0.122900
# dtype: float64

# 层次化索引在数据重塑和基于分组的操作中扮演着重要的角色
# 这段数据可以通过其unstack方法被重新安排到一个DataFrame中
print(data.unstack())
#           1         2         3
# a -0.009437  0.671878  0.528741
# b  0.279347 -0.663702 -0.649679
# c -0.951580  0.693775       NaN
# d       NaN  1.480137 -0.812516

# unstack的逆运算是stack
print(data.unstack().stack())
# a  1    0.589613
#    2    1.017425
#    3   -0.709786
# b  1    1.329885
#    2   -0.666365
#    3    1.390972
# c  1   -0.433534
#    2    1.719552
# d  2    0.201291
#    3    0.749697
# dtype: float64

# 对于DataFrame，每条轴都可以有分层索引
frame = DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
print(frame)
#      Ohio     Colorado
#     Green Red    Green
# a 1     0   1        2
#   2     3   4        5
# b 1     6   7        8
#   2     9  10       11

# 各层索引都可以有名字
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11

# 可以选取列分组
print(frame['Ohio'])
# key1 key2
# a    1         0    1
#      2         3    4
# b    1         6    7
#      2         9   10
