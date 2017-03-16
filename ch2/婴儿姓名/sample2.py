import pandas as pd;
import matplotlib.pyplot as plt;

years = range(1880,2011);
pieces = [];
columns = ["name","sex","births"];
for year in years:
    path = "D:/py/DataAnalysis/pydata-book-master/ch02/names/yob%d.txt" % year;
    frame = pd.read_csv(path,names=columns);
    frame["year"] = year;
    pieces.append(frame);
# 将所有文件读到一个列表里，并添加一列 年份

names = pd.concat(pieces,ignore_index=True);
# 整合到一个DataFrame中
# print(names);

totalBirths = pd.pivot_table(data=names,values="births",index="year",columns="sex",aggfunc="sum");
# 按照年份和性别分组，并对于每个年份和性别求和
print(totalBirths.tail());
# 返回后5行数据
totalBirths.plot(title="Total births by sex and year");
plt.show();


