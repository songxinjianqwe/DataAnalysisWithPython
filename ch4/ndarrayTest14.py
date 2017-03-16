#coding=utf-8
import numpy as np;

arr = np.random.randn(8);
print(arr);
arr.sort();
# 原地调整数组元素顺序
print(arr);

arr2 = np.random.randn(8);
print(arr2);
arr2 = np.sort(arr2);
print(arr2);
#返回排好序的数组的副本


