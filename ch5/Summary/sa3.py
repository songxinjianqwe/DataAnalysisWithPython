from pandas import Series, DataFrame;
import pandas as pd;
import numpy as np;

series = Series(list("cadaabbcc"));
print(series);
# 还有一类方法可以从Series的值中抽取信息
# 返回Series中的唯一值数组
uniques = series.unique();
print(uniques);
# ['c' 'a' 'd' 'b']
# 可以继续排序
uniques.sort();
print(uniques);
# ['a' 'b' 'c' 'd']

# value_counts 用于计算一个Series中各值出现的频率
print(series.value_counts());
# a    3
# c    3
# b    2
# d    1
# dtype: int64


# 为了便于查看，结果Series是按值频率降序排列的
# value_counts还有一个顶级的pandas方法，可用于任何数组或序列
print(series.values);
# ['c' 'a' 'd' 'a' 'a' 'b' 'b' 'c' 'c']
# 设置为不按频数排序
print(pd.value_counts(series.values,sort=False));

# isin方法是对每个元素判断是否在给出的集合中，返回一个布尔型Series
mask = series.isin(["b","c"]);
print(mask);

