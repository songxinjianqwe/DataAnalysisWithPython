import pandas as pd;
from pandas import Series,DataFrame;

data1 = {"Ohio":35000,"Oregen":16000,"Texas":71000,"Utah":5000};
series1 = Series(data1);

data2 = {"California":None,"Ohio":35000,"Oregen":16000,"Texas":71000};
series2 = Series(data2);

# Series最重要的一个功能是：在算术运算中会自动对齐不同的索引的数据
series3 = series1 + series2;
# 如果都有该索引，那么值为两个值之和；如果只有一个，那么仍添加至结果Series中
print(series3);
print("name",series3.name);
print("index.name",series3.index.name);
# 没有指定过的全为None
series3.name = "population";
series3.index.name = "state";
print(series3);
# 会在索引列显示一个表头，为index.name；在最后一行会显示name

# 可以直接通过对属性赋值的方式修改Series的索引
series3.index = ["Bob","Steve","Jeff","Ryan","John"];
print(series3);



