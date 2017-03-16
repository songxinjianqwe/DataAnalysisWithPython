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

# -----------------------------------------------------------

getLastLetter = lambda x:x[-1];
lastLetters = names.name.map(getLastLetter);
lastLetters.name = "lastLetter";
table = pd.pivot_table(data=names,values="births",index=lastLetters,columns=["sex","year"],aggfunc=sum);
# 有多个列的结果：属性名是这几个列的所有取值的排列组合
# print(table);

subTable = table.reindex(columns=[1910,1960,2010],level="year");
# print(subTable);

letterProp = subTable/subTable.sum();
fig,axes = plt.subplots(2,1,figsize=(10,8));
letterProp["M"].plot(kind="bar",rot=0,ax=axes[0],title="Male");
letterProp["F"].plot(kind="bar",rot=0,ax=axes[1],title="Female");
plt.show();
