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
getLastLetter = lambda x:x[-1];
lastLetters = names.name.map(getLastLetter);
lastLetters.name = "lastLetter";
table = pd.pivot_table(data=names,values="births",index=lastLetters,columns=["sex","year"],aggfunc=sum);
subTable = table.reindex(columns=[1910,1960,2010],level="year");
letterProp = subTable/subTable.sum();
# -----------------------------------------------------------
dnyTS = letterProp.ix[["d","n","y"],"M"].T;
print(dnyTS);
dnyTS.plot();
plt.show();
# 各年出生的男孩中名字以d、n、y结尾的人数比例



