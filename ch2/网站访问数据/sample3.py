from pandas import DataFrame;
import json;
import matplotlib.pyplot as plt

path = "../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt";
with open(path) as data:
    records = [json.loads(line) for line in data];

frame = DataFrame(records);
#去除缺省值和空串
cleanTz = frame['tz'].fillna("Missing");#将该属性的缺省值填充为参数
cleanTz[cleanTz == ""] = "Unknown";#【】中接受一个bool，并进行隐式迭代，如果对象的值为空，则赋为Unknown
tzCounts = cleanTz.value_counts();#统计重复次数
# print(tzCounts[:10]);
tzCounts[:10].plot(kind="barh",rot=0);#制图
plt.show();


