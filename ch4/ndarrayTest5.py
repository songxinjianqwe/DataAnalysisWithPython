import numpy as np;

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"]);
data = np.random.randn(7, 4);
# 生成7行4列的一个数组，数组中的元素平均值在0~1，符合正态分布
print(names);
print(data);
print();
# 同算术运算，数组的比较运算也是矢量化，返回结果是一个同样维度的数组，且数组元素类型是bool
# print(names == "Bob");
# 这个布尔型数组可以作为数组索引，布尔型数组必须与被索引的轴长度一致。

# print(data[names == "Bob"]);
# data的第一维长度为7，names的长度也为7，返回的结果：进行一次该长度的遍历，如果返回为True，那么保留原数组的对应低一级数组，否则去除
# 相当于隐式迭代+筛选

# print(data[names == "Bob", 2:]);
# 布尔型索引还可以与切片、整数一起使用
# 在这里，布尔型索引是对第一维进行限制，处理完毕后，切片对第二维进行限制

print(data[(names == "Bob") | (names == "Will")]);
# 注意，组合多个条件表达式只能使用&和|，不能使用and 和or

data[data < 0] = 0;
# 隐式迭代，批量操作
print(data);

