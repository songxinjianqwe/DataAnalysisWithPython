import pandas as pd;
from pandas import DataFrame, Series;
import numpy as np;

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]
        };
frame = DataFrame(data, columns=["year", "state", "pop", "debt"], index=["one", "two", "three", "four", "five"]);
# 指定行和列的名称
frame.index.name = "year";
frame.columns.name = "state";
print(frame);
# 展示效果如下

# state  year   state  pop debt
# year                         
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN

# values属性会以ndarray的形式返回DataFrame中的数据
print(frame.values);
# 展示效果如下

#[[2000 'Ohio' 1.5 nan]
# [2001 'Ohio' 1.7 nan]
# [2002 'Ohio' 3.6 nan]
# [2001 'Nevada' 2.4 nan]
# [2002 'Nevada' 2.9 nan]]

