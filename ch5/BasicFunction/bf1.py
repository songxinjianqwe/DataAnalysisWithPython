import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;

obj = Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"]);
print(obj);
obj2 = obj.reindex(["a", "b", "c", "d", "e"]);
# reindex会根据新索引进行重排。如果某个索引值不存在，就引入缺省值
# 顺序也会变为新的顺序
print(obj2);

# 可以为缺省值赋一个指定的值，比如0
obj2 = obj.reindex(["a", "b", "c", "d", "e"], fill_value=0);
print(obj2);
# 对于时间序列这样的有序数据，重新索引时可以需要做一些插值处理
# method选项即可达到此目的
# 比如fill，可以实现前向值填充
obj3 = Series(["blue", "purple", "yellow"], index=[0, 2, 4]);
print(obj3);
obj3 = obj3.reindex(range(6), method="ffill");
print(obj3);
# 打印结果：

# 0      blue
# 2    purple
# 4    yellow
# dtype: object

# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    yellow
# 5    yellow
# dtype: object

#method 取值有ffil，前向填充值
#bfill，后向填充值
