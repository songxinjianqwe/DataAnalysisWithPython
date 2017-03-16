import pandas as pd;
from pandas import DataFrame, Series;
import numpy as np;

obj = Series(range(3),index=["a","b","c"]);
print(obj);
# pandas 的索引对象负责管理轴标签和其他元数据metadata
# 构建Series或DataFrame时，所用到的数据或其他序列标签都会被转换成一个Index
index = obj.index;
print(index);
# Index(['a', 'b', 'c'], dtype='object')
print(index[1:]);
# Index(['b', 'c'], dtype='object')

# Index对象是不可修改的
index2 = pd.Index(np.arange(3));
obj2 = Series([1.5,-2.5,0],index=index2);
print(obj2.index is index2);
print("----------------------------");

# Index的功能类似于一个固定大小的集合
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]
        };
frame = DataFrame(data, columns=["year", "state", "pop", "debt"], index=["one", "two", "three", "four", "five"]);
print(frame);
print("state" in frame.columns );
print("four" in frame.index);
