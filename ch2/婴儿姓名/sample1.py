import pandas as pd;
path = "D:/py/DataAnalysis/pydata-book-master/ch02/names/yob1880.txt";
namesOf1880 = pd.read_csv(path,names=["name","sex","births"]);
# 将用逗号分隔的数据读出来，并以names作为每列的属性名
# print(namesOf1880);
print(namesOf1880.groupby("sex").births.sum());
# 得到孩子按性别分组的数量，求和


