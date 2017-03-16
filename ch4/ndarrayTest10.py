# coding=utf-8
import numpy as np;

xArr = np.array([1.1,1.2,1.3,1.4,1.5]);
yArr = np.array([2.1,2.2,2.3,2.4,2.5]);
cond = np.array([True,False,True,True,False]);
#纯python 实现，效率较低，且不适用于多维数组
result = [(x if c else y) for x,y,c in zip(xArr,yArr,cond)];
print(result);

# zip([seql, ...])接受一系列可迭代对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
# 一种更好的实现
result2 = np.where(cond,xArr,yArr);
print(result2);
arr = np.random.randn(4,4);
print(arr);
# 第二个和第三个参数可以是标量
# where通常用于根据一个数组生成另一个数组
arr = np.where(arr > 0, 2,-2);
print(arr);

