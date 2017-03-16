import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

series = Series(range(4),index=list("dabc"));
print(series);
# 按索引排序，默认是按照字典序
print(series.sort_index());

frame = DataFrame(np.arange(8).reshape((2,4)),index=["three","one"],columns=list("dabc"));
print(frame);
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7

# 按行索引排序
print(frame.sort_index(axis=0));
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3

# 按列属性排序
print(frame.sort_index(axis=1));
#        a  b  c  d
# three  1  2  3  0
# one    5  6  7  4

# 默认是升序的，如果要修改为降序，可以加一个ascending参数
print(frame.sort_index(axis=1,ascending=False));

# 如果要对Series的数值进行排序，可以使用sort_values方法，默认升序
series = Series([4,7,-3,2]);
print(series);
print(series.sort_values());


# 在排序时，任何缺省值都会被放到Series的末尾
# 表示空值，需要使用numpy的nan成员属性
series2 = Series([4,np.nan,7,np.nan,-3,2]);
print(series2.sort_values());

# 对DataFrame的值进行排序时，可以根据一个或多个列的值进行排序
frame2 = DataFrame({"b":[4,7,-3,2],"a":[0,1,0,1]});
print(frame2);
print(frame2.sort_values(by="b"));
# 先按a列排序，相同的再按b列排序
print(frame2.sort_values(by=["a","b"]));

# 排名：会增设一个排名值，从1开始，一直到数组中有对数据的数量
# 可以根据某种规则破坏平级关系
# rank是为各组分配一个平均排名的方式破坏平级关系的
series3 = Series([7,-5,4,2,0,4]);
print(series3);
# rank默认method是average。实际上与数值有关，数值越大，rank值越大
print(series3.rank());
# 0    6.0
# 1    1.0
# 2    4.5
# 3    3.0
# 4    2.0
# 5    4.5
# dtype: float64

print(series3.rank(method="first"));
# 按值在原始数据中的出现顺序分配排名

# 也可以按降序排名
# max 是使用整个分组的最大排名，min是使用整个分组的最小排名
print(series3.rank(ascending=False,method="max"));




