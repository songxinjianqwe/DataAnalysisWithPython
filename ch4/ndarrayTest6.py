import numpy as np;
arr = np.empty((8,4));
for i in range(8):
    arr[i] = i;
# print(arr);

# print(arr[[4,3,0,6]]);
# 相当于 [arr[4],arr[3],arr[0],arr[6]]

# print(arr[[-3,-5,-7]]);
# 负数索引 -i 就 相当于 len(arr) -i

arr2 = np.arange(32).reshape((8,4));
# 8 行 4列，值从0~31
print(arr2);
print();
print(arr2[[1,5,7,2],[0,3,1,2]]);
# 相当于[arr2[1][0],arr2[5][3],arr2[7][1],arr2[2][2]]
# 要求是两个数组的长度相同，结果集的元素个数等同于数组的长度
print();
print(arr2[np.ix_([1,5,7,2],[0,3,1,2])]);
# 相当于[
#        [arr2[1,0],arr2[1,3],arr2[1,1],arr2[1,2]],
#        [arr2[5,0],arr2[5,3],arr2[5,1],arr2[5,2]],
#        [arr2[7,0],arr2[7,3],arr2[7,1],arr2[7,2]],
#        [arr2[2,0],arr2[2,3],arr2[2,1],arr2[2,2]]        
#      ]
# 两个数组的长度不一定要相等，结果集的元素个数等于两个数组的长度乘积
print();
print(arr2[np.ix_([1,5,7,2],[0,3])]);





