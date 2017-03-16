#coding=utf-8
import numpy as np;
from numpy.linalg import *;

# 矩阵乘法
x = np.array([[1,2,3],[4,5,6]]);
# 2x3
y = np.array([[3,2],[5,6],[8,7]]);
# 3x2

print(x.dot(y));
# 结果应为2x2
# 或者这样写
print(np.dot(x,y));
print();

# numpy.linalg 中有一组标准的矩阵分解运算以及求逆和行列式之类的函数
mat1 = np.arange(25).reshape(5,5);
print(mat1);
print(mat1.dot(mat1.T));
print(mat1);
# A*A-1 = E
print();

mat2 = np.random.randn(3,3);
print(mat2);
print(inv(mat2));
