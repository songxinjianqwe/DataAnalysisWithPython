from pandas import DataFrame, Series;
import json;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

path = "../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt";
with open(path) as data:
    records = [json.loads(line) for line in data];
frame = DataFrame(records);
userFrame = frame[frame.a.notnull()];  # 筛选，隐式迭代，去掉数据集中该属性为空的记录
osList = np.where(userFrame["a"].str.contains("Windows"), "Windows", "Not Windows");
# 隐式迭代，如果数据集的该属性的值中含有某字符串，则将参数2放入结果，否则将参数3放入结果。结果是一个列表
byTZOS = userFrame.groupby(['tz', osList]);
# 按照tz属性和列表中的值进行分组，最终有tz的所有取值和osList的所有取值的排列组合这么多组
aggCounts = byTZOS.size().unstack().fillna(0);#size类似于value_counts() 统计重复，得到一个Series对象，unstack是将分组后地数据组织成二维表的格式

# print(aggCounts[:10]);
#打印出来是二维表的格式
indexer = aggCounts.sum(1).argsort(); 
#sum是求和，参数是index，第几个属性，得到每个属性的出现次数。argsort是按该属性的出现次数排序
# print(indexer[:10]);  
# 最常出现的时区，前10个，只含时区属性

countSubSet = aggCounts.take(indexer[-10:]);#取出后10行 ，实际的开始下标是len()-10。然后至末尾，即后10个。
# print(countSubSet);
countSubSet.plot(kind="barh",stacked=True);
plt.show();


