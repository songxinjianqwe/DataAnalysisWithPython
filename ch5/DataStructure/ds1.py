from pandas import Series, DataFrame;
import pandas as pd;
import numpy as np;

# Series 类似于一维数组，它由一组数据（Numpy数组类型）以及一组与之相关的数据标签（索引）组成
# Series 级数;系列，连续
obj = Series([4, 2, 3, 1]);
print(obj);
# 打印时：索引在左边，值在右边
# 如果没有为数据指定索引，于是会自动创建一个0~N-1的整数型索引
# 可以分别取得值和索引
print(obj.values);
print(obj.index);
print();

# 手动指定索引
obj2 = Series([4, 2, 3, 1], index=['d', 'a', 'c', 'b']);
print(obj2);
print(obj2.values);
print(obj2.index);
# 可以通过索引来选取Series的单个或一组值
print(obj2['a']);
obj2['d'] = 121;
print(obj2);

# 打印形式同直接打印obj2
# 选取多个值是放到下标的下标里
print(obj2[['a', 'c', 'd']]);

# 下标还可以执行过滤、计算操作，实际执行的是元素级的操作
print(obj2[obj2 > 3]);
print("---------------------------");
# 可以直接使用加减乘除算术符号
obj2 = obj2*2;
print(obj2);



