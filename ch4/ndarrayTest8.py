# coding-utf-8
import numpy as np;
import matplotlib.pyplot as plt ;
# 用数组表达式代替循环的做法，称为矢量化。
# Numpy数组可以将多种数据处理表述为简洁的数组表达式

# 在一组值上计算函数sqrt(x^2+y^2)
# np.meshgrid()函数接受两个一维数组，并产生两个二维矩阵
# 1000个间隔相等的点
# arange生成一个一维数组，-5~5，每隔0.01生成一个数字，一共有1000个数字
points = np.arange(-5, 5, 0.01);
xs,ys = np.meshgrid(points,points);
print(xs);
print(ys);
# 第一个返回值是将第一个参数在行上重复，变为方阵
# 第二个返回值是将第二个参数在列上重复，变为方阵
# para1 = [1,2,3] para2 = [4,5,6]
# result1 = [
#    [1,2,3],
#    [1,2,3],
#    [1,2,3]
# ]

# result2 = [
#    [4,4,4],
#    [5,5,5],
#    [6,6,6]
# ]


z = np.sqrt(xs ** 2 + ys ** 2);
print(z);
plt.imshow(z,cmap=plt.cm.gray);
plt.colorbar();
plt.title("Image plot of sqrt(x^2+y^2) for a grid of values");
plt.show();
