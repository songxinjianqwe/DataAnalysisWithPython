#coding=utf-8
import numpy as np;

arr  = np.arange(10);
print(arr);
#开方
arr2 = np.sqrt(arr);
print(arr2);
#计算各元素的指数x -> exp(x)
arr3 = np.exp(arr);
print(arr3);
arr4 = np.random.randn(8);
print(arr4);
arr5 = np.random.randn(8);
print(arr5);
# 两个参数的维度是一样的，对每个元素取较大的值
arr6 = np.maximum(arr4,arr5);
print(arr6);
print();

arr7 = np.random.randn(8) * 5;
print(arr7);
# 结果是一个元组，第一个元素是小数数组，第二个元素是整数数组
arr8 = np.modf(arr7);
print(arr8);



