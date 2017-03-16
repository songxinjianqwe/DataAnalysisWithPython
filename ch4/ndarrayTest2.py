import numpy as np;
arr1 = np.array([1,2,3],dtype=np.float64);
print(arr1.dtype);
# 创建时可以指定数据类型
arr2 = np.array([4,5,6],dtype=np.int64);
# astype会拷贝一个新数组
print(arr2.dtype);

floatArr2 = arr2.astype(np.float64);
print(floatArr2.dtype);

arr3 = np.array([3.6,2,-2.1,0.5]);
intArr3 = arr3.astype(np.int32);
print(intArr3);
# 会截断小数位，只保留整数



