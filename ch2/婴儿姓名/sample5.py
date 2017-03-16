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
# ----------------------------------------------------------------------------------
boys = top1000[top1000.sex == "M"];
girls = top1000[top1000.sex == "F"];
# totalBirths = pd.pivot_table(data=top1000,values="births",index="year",columns="sex",aggfunc=sum);
# print(totalBirths[:5]);
totalProp = pd.pivot_table(data=top1000,values="prop",index="year",columns="sex",aggfunc=sum);
totalProp.plot(title="Sum of table1000.prop by year and sex",yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10));
plt.show();


