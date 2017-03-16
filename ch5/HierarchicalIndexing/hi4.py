from pandas import DataFrame, Series
import numpy as np

# 将DataFrame的一个或多个列当做索引来使用，或者希望将索引变成DataFrame的列
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)
#    a  b    c  d
# 0  0  7  one  0
# 1  1  6  one  1
# 2  2  5  one  2
# 3  3  4  two  0
# 4  4  3  two  1
# 5  5  2  two  2
# 6  6  1  two  3

# set_index函数会将其一个或多个列转为行索引，并创建一个新的DataFrame
frame2 = frame.set_index(['c', 'd'])
print(frame2)
#        a  b
# c   d
# one 0  0  7
#     1  1  6
#     2  2  5
# two 0  3  4
#     1  4  3
#     2  5  2
#     3  6  1
# 默认情况下，那些列会从DataFrame中移除，但可以选择将其保留下来
frame3 = frame.set_index(['c', 'd'], drop=False)
print(frame3)
#        a  b    c  d
# c   d
# one 0  0  7  one  0
#     1  1  6  one  1
#     2  2  5  one  2
# two 0  3  4  two  0
#     1  4  3  two  1
#     2  5  2  two  2
#     3  6  1  two  3

# reset_index的功能跟set_index刚好相反，层次化索引的级别会被转移到列里面
print(frame2.reset_index())
#      c  d  a  b
# 0  one  0  0  7
# 1  one  1  1  6
# 2  one  2  2  5
# 3  two  0  3  4
# 4  two  1  4  3
# 5  two  2  5  2
# 6  two  3  6  1

