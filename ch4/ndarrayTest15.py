#coding=utf-8
import numpy as np;
names = np.array(["Bob","Joe","Will","Bob","Will","Joe","Joe"]);
print(names);
names = np.unique(names);
print(names);


arr1 = [2,3,4];
arr2 = [3,4,5];
# 取交集
intersectedArr = np.intersect1d(arr1,arr2);
print(intersectedArr);
# 取并集
unionedArr= np.union1d(arr1,arr2);
print(unionedArr);

src = [6,0,0,3,2,5,6];
dest = [2,3,6];
print(np.in1d(src,dest));
# 返回和src数组相同长度的布尔型数组
# 如果src[i]在dest数组中，那么result[i]为True，否则为False

