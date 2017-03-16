import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

obj = Series(np.arange(4),index=["a","b","c","d"]);
print(obj);
# 通过索引来获取某一行（按index取值）
print(obj["a"]);
# 可以使用切片，切片值可以是整数索引（从0开始），也可以是自定义的index值
print(obj[1:3]);
# 取多列
print(obj[[1,3]]);
print(obj[["a","d"]]);
# 可以使用下标进行筛选
print(obj[obj > 2]);

# 注意，使用index值进行切片时，末端是包含的
print(obj["a":"c"]);
# a    0
# b    1
# c    2
# dtype: int32

# 批量赋值操作
obj["b":"c"] = 999;
print(obj);
# a      0
# b    999
# c    999
# d      3
# dtype: int32

print("---------------------------------------");

data = DataFrame(np.arange(16).reshape((4,4)),index=["Ohio","Colorado","Utah","New York"],columns=["one","two","three","four"]);
print(data);

# 可以对DataFrame进行行方向或列方向的切片、过滤、赋值
# 直接使用下标是对列方向进行筛选，只留下选中的列
print(data["two"]);
print(data[["three","one"]]);

# 选取行有两种方式，一种是切片，另一种是ix方法
# 对于Series而言，不论下标中写出具体index，还是使用切片，都是对行进行操作
# 对于DataFrame而言，下标中写出具体的column，是对列进行操作；使用切片，是对行进行操作

print(data[:2]);
print(data[:"Utah"]);
# print(data[["Utah","Colorado"]]); 不合法

print(data < 5);
# data < 5 返回的是与data同样大小的布尔型数组
# 如果下标中放入一个相同大小的布尔型数组，那么迭代时如果对应的布尔值是True，则选中；否则不选中
data[data < 5] = 0;
print(data);
# DataFrame 的语法更类似于ndarray


# 另一种对行进行操作的方式，同时可以对列进行操作
# 第一个参数是新的行索引，第二个参数是新的列属性
# 注意ix不是一个方法，而是接受一个下标
print(data.ix["Colorado",["two","three"]]);
print(data.ix[["Colorado","Utah"],[3,0,1]]);
print("----------------------------------------------");
print(data);
# 取出第二行
print(data.ix[2]); 
# 取出前三行，取第二列
print(data.ix[:"Utah","two"]);
# 对每一行的three这一列进行筛选，不符的直接去掉这一行，剩余的行取前三列
print(data.ix[data.three > 3,:3]);

print("----------------------------------------------");
print(data);
# 取一行
print(data.ix["Ohio"])
# 取一列
print(data.ix[:,"one"]);
