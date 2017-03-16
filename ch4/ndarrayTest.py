import numpy as np;
list = [6,5,3,2,1.,0];
arr1 = np.array(list);
print(arr1);
print(arr1.dtype);
print(arr1.shape);
print(arr1.ndim);
print();

list2 = [[1,2,3,4],[5,6,7,8]];
arr2 = np.array(list2);
print(arr2);
print(arr2.dtype);
print(arr2.shape);
print(arr2.ndim);
print();

arr3 = np.zeros(10);
print(arr3);
print(arr3.dtype);
# 数据类型默认是float64

arr4 = np.zeros((3,6));
#得到一个二维的，3个 具有6个元素的数组
print(arr4);
print();

arr5 = np.empty((2,3,2));
#得到一个三维的没有具体值的数组，默认是垃圾值
print(arr5);

arr6 = np.arange(10);
# arange是range函数的数组版
print(arr6);


