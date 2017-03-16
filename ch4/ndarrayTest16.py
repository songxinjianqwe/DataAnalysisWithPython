#coding=utf-8
import numpy as np;

arr = np.arange(10);
print(arr);
# 将数组以二进制形式写入到文件中，默认扩展名为npy
np.save("some_array",arr);

arr2 = np.load("some_array.npy");
print(arr2);
