from pandas import DataFrame,Series;
import json;
import matplotlib.pyplot as plt

path = "../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt";
with open(path) as data:
    records = [json.loads(line) for line in data];
frame = DataFrame(records);
results = Series([x.split()[0] for x in frame['a'].dropna()]);#去掉数据集中该属性为缺省值的记录，然后取出属性值中的第一个空格以前的部分，放到一个Series中
browserCounts = results.value_counts();#统计重复
print(browserCounts[:10]);

