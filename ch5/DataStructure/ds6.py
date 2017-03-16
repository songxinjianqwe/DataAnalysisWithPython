import numpy as np;
import pandas as pd;
from pandas import Series,DataFrame;

# 另一种构造DataFrame的方式是嵌套字典
pop = {"Nevada":{2001:2.4,2002:2.9},
       "Ohio":{2000:1.5,2001:1.7,2002:3.6}};
# 外层字典的键是列名，内层字典的键是行索引
# 如果内层字典的行索引不同，那么取并集，没有值的填入Nan
frame = DataFrame(pop);
print(frame);
# 行列互换，转置
print(frame.T);
print("----------------------------------");
# 也可以显式指定索引
frame2 = DataFrame(pop,index=[2000,2001,2002]);
print(frame2.T);

print("--------------------------------------");
# frame[]返回的是一个字典，键是索引，值是该列的值
pdata = {"Ohio":frame2["Ohio"],
         "Nevada":frame2["Nevada"]};
frame3 = DataFrame(pdata);
print(frame3);
