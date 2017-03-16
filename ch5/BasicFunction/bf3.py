import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

# 丢弃指定轴上的项
obj = Series(np.arange(5),index=["a","b","c","d","e"]);
print(obj);
# 删除某一行
obj2 = obj.drop("c");
print(obj2);
# 删除多行
obj3 = obj.drop(["d","c"]);
print(obj3);

data = DataFrame(np.arange(16).reshape((4,4)),index=["Ohio","Colorado","Utah","New York"],columns=["one","two","three","four"]);
print(data);
print(data.drop(["Colorado","Ohio"]));

