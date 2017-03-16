import pandas as pd;
from pandas import Series,DataFrame;
obj = Series([1,2,3,4],index=["a","b","c","d"]);
print(obj);
# 可以将Series视为一个dict，键是索引，值是值
print("a" in obj);
print("dd" in obj);
# 可以通过字典来创建Series
# 如果只传入一个字典，那么结果中的索引就是字典的键（有序）
personDict = {"name":"sinjinsong","age":12,"school":"NJU"};
person = Series(personDict);
print(person);
states = ["California","Ohio","Oregon","Texas"];
sdata = {"Ohio":35000,"Texas":71000,"Oregen":16000,"Utah":5000};
obj2 = Series(sdata,index=states);
# 如果用一个字典和一个列表作为参数，那么会将列表作为索引，然后将列表中的每个值作为key到字典中找值，如果没有，那么为Nan，如果找到，则为对应的值
print(obj2);
# 只有Texas和Ohio有值，California和Oregen没有值

# 检测缺失数据
print(pd.isnull(obj2));
# 返回一个Series，索引仍为obj2的索引，值都为bool型，有值的为True，没有值的为False
print(pd.notnull(obj2));
# 和上一个函数的返回值相反

# 自己的实例方法
print(obj2.isnull());




