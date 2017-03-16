import numpy as np
from scipy.optimize import leastsq
# 原始点集
x = np.array([36.9, 46.7, 63.7, 77.8, 84.0, 87.5])
y = np.array([181, 197, 235, 270, 283, 292])


# 待拟合函数
# 一次函数
def f(p, x):
    k, b = p
    return k * x + b

# 实验数据x、y和拟合函数之间的差值
def error(p, x, y):
    return f(p, x) - y


# 待拟合的点
n0 = [3, 20]
para = leastsq(error, n0, args=(x, y))
# 实验数据拟合后的参数
k, b = para[0]
print(k, b)
