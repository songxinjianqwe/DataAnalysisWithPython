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

def addProp(group):
    births = group.births;
    group['prop'] = births/ births.sum();
    return group;
names= names.groupby(["year","sex"]).apply(addProp);
# ----------------------------------------------------------------------------------

def getTop1000(group):
    return group.sort_values(by="births",ascending=False)[:1000];
top1000 = names.groupby(["year","sex"]).apply(getTop1000);
# 取出每对year/sex 组合的前1000个名字
print(top1000);

