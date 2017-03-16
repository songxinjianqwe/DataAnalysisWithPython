from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# pandas提供了一些用于将表格型数据读取为DataFrame对象的函数
# 最常用的是read_csv和read_table
# 函数的选项可以划分为以下几个大类：

# 索引：将一个或多个列当做返回的DataFrame，以及是否从文件、用户获取列名
# 类型推断和数据转换
# 日期解析
# 迭代：支持对大文件进行逐块迭代
# 不规整数据问题：跳过一些行、页脚、注释
pathEx1 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex1.csv"
pathEx2 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex2.csv"
pathMindEx = "D:/py/DataAnalysis/pydata-book-master/ch06/csv_mindex.csv"
pathEx3 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex3.csv"
pathEx4 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex4.csv"
pathEx5 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex5.csv"

frame = pd.read_csv(pathEx1)
print(frame)
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

# 也可以使用read_table,但要手动指定分隔符
frame2 = pd.read_table(pathEx1, sep=',')
print(frame2)

# ex2文件没有标题行（表头），可以自己定义列名
frame3 = pd.read_csv(pathEx2, names=["a", "b", "c", "message"])
print(frame3)
#     a   b   c message
# 1   2   3   4   hello
# 5   6   7   8   world
# 9  10  11  12     foo

# 可以选择将一列作为索引列，index_col的参数从1开始
frame4 = pd.read_csv(pathEx2, names=["a", "b", "c", "message"], index_col=4)
print(frame4)
#        a   b   c  message
# hello  1   2   3        4
# world  5   6   7        8
# foo    9  10  11       12

# 将多个列作为层次化索引
# 源文件
# key1,key2,value1,value2
# one,a,1,2
# one,b,3,4
# one,c,5,6
# one,d,7,8
# two,a,9,10
# two,b,11,12
# two,c,13,14
# two,d,15,16

frame5 = pd.read_csv(pathMindEx, index_col=['key1', 'key2'])
print(frame5)
#            value1  value2
# key1 key2
# one  a          1       2
#      b          3       4
#      c          5       6
#      d          7       8
# two  a          9      10
#      b         11      12
#      c         13      14
#      d         15      16

# 可以编写一个正则表达式来作为read_table的分隔符
#             A         B         C
# aaa -0.264438 -1.026059 -0.619500
# bbb  0.927272  0.302904 -0.032399
# ccc -0.264273 -0.386314 -0.217601
# ddd -0.871858 -0.348382  1.100491

frame6 = pd.read_table(pathEx3, sep='\s+')
print(frame6)
#             A         B         C
# aaa -0.264438 -1.026059 -0.619500
# bbb  0.927272  0.302904 -0.032399
# ccc -0.264273 -0.386314 -0.217601
# ddd -0.871858 -0.348382  1.100491

# 由于列名行中有内容的字段的数量比其他数据行中有内容的字段数量少1，所以read_table将第一列作为索引

# 读文件时跳过某些行
# # hey!
# a,b,c,d,message
# # just wanted to make things more difficult for you
# # who reads CSV files with computers, anyway?
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo

frame7 = pd.read_csv(pathEx4, skiprows=[0, 2, 3])
print(frame7)
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

# 缺失值处理
# 源文件
# something,a,b,c,d,message
# one,1,2,3,4,NA
# two,5,6,,8,world
# three,9,10,11,12,foo

frame8 = pd.read_csv(pathEx5)
print(frame8)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo

print(pd.isnull(frame8))
#   something      a      b      c      d message
# 0     False  False  False  False  False    True
# 1     False  False  False   True  False   False
# 2     False  False  False  False  False   False
frame9 = pd.read_csv(pathEx5, na_values=['NULL'])
print(frame9)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo

# 可以用一个字典为各列指定不同的NA标记值

sentinels = {"message": ['foo', 'na'], 'something': ['two']}

frame10 = pd.read_csv(pathEx5, na_values=sentinels)
print(frame10)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       NaN  5   6   NaN   8   world
# 2     three  9  10  11.0  12     NaN
