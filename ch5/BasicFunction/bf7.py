import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

# 举个栗子
# 二维数组和它的某一行相减
arr = np.arange(12).reshape(3,4);
print(arr);
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(arr - arr[0]);
# [[0 0 0 0]
#  [4 4 4 4]
#  [8 8 8 8]]
# 实际效果是每一行都减去了第一行，对应列的元素相减
# [[0-0 1-1 2-2 3-3]
#  [4-0 5-1 6-2 7-3]
#  [8-0 9-1 10-2 11-3]]

# 这称为广播

frame = DataFrame(np.arange(12).reshape((4,3)),columns=list("bde"),index=["Utah","Ohio","Texas","Oregen"]);
print(frame);
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregen  9  10  11
series = frame.ix[0];
print(series);
# b    0
# d    1
# e    2
# frame.ix[下标] 是取一行
print(frame-series);
#         b  d  e
# Utah    0  0  0
# Ohio    3  3  3
# Texas   6  6  6
# Oregen  9  9  9
