from pandas import Series, DataFrame;
import pandas as pd;
import numpy as np;

# pandas对象有一组常用的数学和统计方法，大部分都属于约简和汇总统计，用于从Series提取单个值，或从DataFrame的行或列中提取一个Series
frame = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=["one","two"]);
print(frame);
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3

print(frame.sum());
# 对每列做一个sum，Nan被视为0
# one    9.25
# two   -5.80
# dtype: float64

print(frame.sum(axis=1));
# 对每行做一个sum
# 
# a    1.40
# b    2.60
# c    0.00
# d   -0.55
# dtype: float64

# 总结一下：axis=0时，返回结果含有属性，对每行进行操作；axis=1时，返回结果含有索引，对每列进行操作

# sum求和时Nan被自动排除，除非整个行/列都是Nan
# 通过skipna可以禁用该功能
print(frame.mean(axis=1,skipna=False));
# a      NaN
# b    1.300
# c      NaN
# d   -0.275
# dtype: float64


print("-------------------------------------------");
print(frame);
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3

# idxmax和idxmin返回的是间接统计，比如返回索引名或属性名，而非值
print(frame.idxmax(axis=0));
# 显示的是属性，计算的是每列的最大值对应的索引名
# one    b
# two    d
# dtype: object

print(frame.idxmin(axis=1));
# 显示的是索引，计算的是每行的最小值对应的属性名
# a    one
# b    two
# c    NaN
# d    two
# dtype: object

# 返回是累计值，默认是对每列自上向下累计
print(frame.cumsum());
#     one  two
# a  1.40  NaN
# b  8.50 -4.5
# c   NaN  NaN
# d  9.25 -5.8

# 对每列属性进行一系列统计
print(frame.describe());
#             one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000


# 对于非数值型数据，describe会产生另外一种汇总统计
series = Series(['a','b','c','d'] * 4);
print(series);
print(series.describe());
# count     16
# unique     4
# top        a
# freq       4
# dtype: object
