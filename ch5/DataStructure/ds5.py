import pandas as pd;
from pandas import DataFrame,Series;
import numpy as np;
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]
        };
frame = DataFrame(data, columns=["year", "state", "pop", "debt"], index=["one", "two", "three", "four", "five"]);
# 为不存在的列赋值会创建出一个新列
frame["eastern"] = frame.state == "Ohio";
print(frame);
# 关键字del用于删除列
del frame["eastern"];
print(frame);
# 通过索引方式获得的Series都是原DataFrame的一个视图。如果想拷贝，需要使用Series的copy方法。
series = frame["state"].copy();
print(series);
series["one"] = "California";
print(series);
print(frame);


