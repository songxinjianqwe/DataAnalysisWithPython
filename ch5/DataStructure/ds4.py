import pandas as pd;
import numpy as np;
from pandas import DataFrame, Series;

# DataFrame是一个表格型的数据结构，含有一组有序的列，每列可以是不同的值类型。
# 既有行索引，又有列索引，可以被看做由Series组成的字典（共用同一个索引）

# 最常见的构造DataFrame的方式是传入一个由等长列表组成的字典
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]
        };
frame = DataFrame(data, columns=["year", "state", "pop", "debt"], index=["one", "two", "three", "four", "five"]);
# 指定columns后按照该顺序组织列，如果columns中含有不存在的列，那么值均为Nan
# 指定index会将默认的从0的开始的整数索引替换为给定的索引
print(frame);

# 获取列名
print(frame.columns);
# 获取某一列的所有数据
print(frame['state']);
# 获取列数据的另一种方式
print(frame.year);
# 获取某一行的所有数据,展示效果同上
print(frame.ix["three"]);

# 对列的值进行元素级的修改
frame["debt"] = 16.5;
print(frame);
# 将列表或数组赋值给某个列时，其长度必须与DataFrame的长度相匹配。
frame["debt"] = np.arange(5);
print(frame);
# 如果赋值的是一个Series，则会精确匹配DataFrame的索引，所有的空位都将被填上缺省值
val = Series([-1.2,-1.5,-1.7],index=["two","four","five"]);
frame["debt"] = val;
print(frame);

