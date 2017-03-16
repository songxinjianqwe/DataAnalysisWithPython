import pandas as pd
import sys
import numpy as np
from pandas import DataFrame, Series
# 将数据写出到文件格式
pathEx5 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex5.csv"
frame = pd.read_csv(pathEx5)
print(frame)
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo
frame.to_csv("out.csv")
# 默认分隔符是,

# 还可以使用其他分隔符
frame.to_csv(sys.stdout, sep='|')
# |something|a|b|c|d|message
# 0|one|1|2|3.0|4|
# 1|two|5|6||8|world
# 2|three|9|10|11.0|12|foo

# 缺失值将被表示为空串，可以将其表示为其他的标记值
frame.to_csv(sys.stdout, na_rep="NULL")
# ,something,a,b,c,d,message
# 0,one,1,2,3.0,4,NULL
# 1,two,5,6,NULL,8,world
# 2,three,9,10,11.0,12,foo


# 如果没有设置，则会写出行和列的标签。也可以去禁用它们
frame.to_csv(sys.stdout, index=False, header=False)
# one,1,2,3.0,4,
# two,5,6,,8,world
# three,9,10,11.0,12,foo
print("--------------------------")

# 还可以只写出一部分的列，并以指定的顺序排列
frame.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
# a,b,c
# 1,2,3.0
# 5,6,
# 9,10,11.0

# Series 也有一个to_csv的方法
dates = pd.date_range('1/1/2000', periods=7)
series = Series(np.arange(7), index=dates)
series.to_csv("series.csv")

dates = Series.from_csv("D:/py/DataAnalysis/ch6/ReadWriteText/series.csv", parse_dates=True)
print(dates)
# 2000-01-01    0
# 2000-01-02    1
# 2000-01-03    2
# 2000-01-04    3
# 2000-01-05    4
# 2000-01-06    5
# 2000-01-07    6
# dtype: int64

