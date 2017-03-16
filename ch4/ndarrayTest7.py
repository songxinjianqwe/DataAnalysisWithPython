import numpy as np;

arr = np.arange(15).reshape((3,5));
print(arr);
# 转置是重塑的一种特殊形式，返回的是原数组的视图
# 有一个transpose方法和一个T属性
# T属性是其转置
print("--------------------------");
print(arr.T);
print("--------------------------");
print(np.dot(arr.T,arr));
# dot方法是做矩阵乘法
