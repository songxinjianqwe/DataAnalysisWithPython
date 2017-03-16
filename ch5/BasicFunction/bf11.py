import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

# 轴索引是可以重复的
series = Series(range(5), index=list("aabbc"));
print(series);
print(series.index.is_unique);
# 如果某个索引对应多个值，则返回一个Series
# 对应单个值的，则返回一个标量值
print(series["a"]);
# a    0
# a    1
# dtype: int32
print(series["c"]);
# 4

# DataFrame 也是如此
frame = DataFrame(np.random.randn(4, 3), index=list("aabb"));
print(frame);
print(frame.ix["a"]);
#           0         1         2
# a  0.639593 -0.064668 -0.176142
# a -0.585803 -0.412077 -0.268721
