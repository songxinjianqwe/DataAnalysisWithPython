import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

frame = DataFrame(np.arange(12).reshape((4,3)),columns=list("bde"),index=["Utah","Ohio","Texas","Oregen"]);
print(frame);
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregen  9  10  11
series = Series(range(3),index=["b","e","f"]);
print(series);
# b    0
# e    1
# f    2

# 如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运算的两个对象就会被重新索引以形成并集
print(frame+series);
#           b   d     e   f
# Utah    0.0 NaN   3.0 NaN
# Ohio    3.0 NaN   6.0 NaN
# Texas   6.0 NaN   9.0 NaN
# Oregen  9.0 NaN  12.0 NaN

# 取一列
series2 = frame["d"];
print(series2);
# Utah       1
# Ohio       4
# Texas      7
# Oregen    10
# 除了+-*/外，还有add，sub，mul，div方法可以调用
# 传入的axis是轴的意思，0表示行
print(frame.sub(series2,axis=0));
#         b  d  e
# Utah   -1  0  1
# Ohio   -1  0  1
# Texas  -1  0  1
# Oregen -1  0  1
# 实际上是第一行全部减去series[0]，第二行全部减去series[1]

