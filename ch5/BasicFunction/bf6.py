import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

frame1 = DataFrame(np.arange(12).reshape((3,4)),columns=list("abcd"));
frame2 = DataFrame(np.arange(20).reshape((4,5)),columns=list("abcde"));
print(frame1);
print(frame2);

print(frame1 + frame2);
#       a     b     c     d   e
# 0   0.0   2.0   4.0   6.0 NaN
# 1   9.0  11.0  13.0  15.0 NaN
# 2  18.0  20.0  22.0  24.0 NaN
# 3   NaN   NaN   NaN   NaN NaN

frame3 = frame1.add(frame2,fill_value=0);
# 如果任何一个表格中对应的值不存在，则替换为0，再与另一个表格中对应的值相加
# print(frame3);
#       a     b     c     d     e
# 0   0.0   2.0   4.0   6.0   4.0
# 1   9.0  11.0  13.0  15.0   9.0
# 2  18.0  20.0  22.0  24.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

# 重新索引时，也可以指定一个填充值
print(frame1.reindex(columns=frame2.columns,fill_value=0));
