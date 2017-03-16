import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

frame = DataFrame(np.random.randn(4,3),columns=list("bde"),index=["Utah","Ohio","Texas","Oregen"]);
print(frame);
#                b         d         e
# Utah    0.706698  1.356374 -0.994024
# Ohio    2.013752  1.793239 -0.288007
# Texas   1.135937  0.007887  0.885167
# Oregen -0.094336  0.244169 -1.290243

# Numpy的ufuncs 元素级数组方法也可以应用于pandas对象
print(np.abs(frame));
#                b         d         e
# Utah    0.706698  1.356374  0.994024
# Ohio    2.013752  1.793239  0.288007
# Texas   1.135937  0.007887  0.885167
# Oregen  0.094336  0.244169  1.290243

# 另一个常见的操作是：将函数运用到各列或行所形成的的一维数组上
func = lambda x:x.max() - x.min();
print(frame.apply(func,axis=0));
# b    2.108089
# d    1.785352
# e    2.175410
# dtype: float64

# 实际上是对每列作为一个数组传入func，然后接受一个返回值，将各列返回值组合起来作为结果
print(frame.apply(func,axis=1));
# Utah      2.350399
# Ohio      2.301760
# Texas     1.128050
# Oregen    1.534412
# dtype: float64

# 对各行执行apply
# 许多常见的数据统计方法都被实现成DataFrame的方法（如sum和mean），因此无需使用apply方法

# 除标量值外，传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return Series([x.max(),x.min()],index=["min","max"]);
print(frame.apply(f,axis=0));
#             b         d         e
# min  2.013752  1.793239  0.885167
# max -0.094336  0.007887 -1.290243

# 也可以使用元素级的python函数，如果想得到每个浮点值的格式化字符串

format = lambda x: '%.2f' % x;
print(frame.applymap(format));
#             b      d     e
# Utah    -1.34   1.32  0.51
# Ohio    -0.02   1.03  0.88
# Texas    1.51  -0.07  1.83
# Oregen  -1.04  -2.76  0.81

# 也可以应用于元素级函数
print(frame["b"].map(format));
# Utah      -0.12
# Ohio      -1.02
# Texas      0.17
# Oregen    -1.61
# Name: b, dtype: object