from pandas import DataFrame;
import json;

path = "../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt";
with open(path) as data:
    records = [json.loads(line) for line in data];
    
frame = DataFrame(records);
# print(frame['tz']);
# print(frame['tz'][:10]);
tzCounts = frame['tz'].value_counts(); #按照出现次数排序，返回为一个键值对的列表，每个元素是该属性值及其出现次数
print(tzCounts);
# print(tzCounts[:10]);




