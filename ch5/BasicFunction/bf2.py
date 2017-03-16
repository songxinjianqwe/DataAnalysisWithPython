import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

frame = DataFrame(np.arange(9).reshape(3, 3), index=["a", "c", "d"], columns=["Ohio", "Texas", "California"]);
print(frame);

# reindex可以修改DataFrame的行索引、列，或两个都修改
# 修改行索引
frame2 = frame.reindex(index=["a", "b", "c", "d"]);
print(frame2);
# 修改列属性
frame3 = frame.reindex(columns=["Texas", "Utah", "California"]);
print(frame3);
# 同时修改行索引和列属性，插值只能按行应用
frame4 = frame.reindex(index=["a", "b", "c", "d"], columns=["Texas", "Utah", "California"], method="ffill");
print(frame4);

# 使用ix的标签索引功能，可以以一种简洁的方式同时修改行索引和列属性
# 第一个参数是行索引，第二个参数是列顺序
frame5 = frame.ix[["a", "b", "c", "d"], ["Texas", "Utah", "California"]];
print(frame5);
