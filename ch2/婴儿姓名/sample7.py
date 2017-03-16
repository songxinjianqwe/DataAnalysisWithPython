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

boys = top1000[top1000.sex == "M"];
girls = top1000[top1000.sex == "F"];
# ----------------------------------------------------------------------------------

df = boys[boys.year == 2010];
# print(df);
propCumsum = df.sort_values(by="prop",ascending=False).prop.cumsum();
# 按比例排序
# print(propCumsum[:10]);
print(propCumsum.searchsorted(0.5)); #找到前50% 的分界

def getQuantileCount(group,q=0.5): # quantile 分位数
    group = group.sort_values(by="prop",ascending=False);
    return group.prop.cumsum().searchsorted(q)[0]+1;
#python3的searchsorted()返回的是ndarray类型
#需要先取[0]元素，才能获得想要的数据，如果不作该处理，绘图会报错
diversity = top1000.groupby(["year","sex"]).apply(getQuantileCount);
diversity = diversity.unstack("sex");
# print(diversity);

# 拿到所有年份的，区分了不同性别的，所对应的占了前50%的分位数
diversity.plot(title="Number of popular names in top 50%");
plt.show();
