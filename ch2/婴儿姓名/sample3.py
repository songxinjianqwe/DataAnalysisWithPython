import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

years = range(1880,2011);
pieces = [];
columns = ["name","sex","births"];
for year in years:
    path = "D:/py/DataAnalysis/pydata-book-master/ch02/names/yob%d.txt" % year;
    frame = pd.read_csv(path,names=columns);
    frame["year"] = year;
    pieces.append(frame);
names = pd.concat(pieces,ignore_index=True);
# ----------------------------------------------------------------------------------
def addProp(group):
    births = group.births;
    group['prop'] = births/ births.sum();
    return group;

names= names.groupby(["year","sex"]).apply(addProp);
# 按年份和性别分组，并且增加一个属性，是指定名字的婴儿数相对于总出生数的比例
print(names);
print(np.allclose(names.groupby(["year","sex"]).prop.sum(),1));
# 校验比例之和是否为1

