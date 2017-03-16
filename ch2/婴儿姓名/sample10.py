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
def getTop1000(group):
    return group.sort_values(by="births",ascending=False)[:1000];
top1000 = names.groupby(["year","sex"]).apply(getTop1000);
# ---------------------------------------------------------------------------

allNames = top1000.name.unique();
mask = np.array(["lesl" in x.lower() for x in allNames]);
lesleyLike = allNames[mask];
# print(lesleyLike);
# 拿到lesl开头的名字

filtered = top1000[top1000.name.isin(lesleyLike)];
# print(filtered);
# 只留下lesl开头的名字

table = pd.pivot_table(data=filtered,values="births",index="year",columns="sex",aggfunc=sum);
table = table.div(table.sum(1),axis=0);
# 按照年份进行统计求和
# print(table);

table.plot(style={"M":"k-","F":"k--"});
plt.show();
