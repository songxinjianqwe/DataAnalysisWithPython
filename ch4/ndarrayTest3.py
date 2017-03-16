import numpy as np;

arr = np.array([[1, 2, 3], [4, 5, 6]]);
res = arr * arr;
print(res);
print("-----------------------");

arr2 = np.arange(10);
print(arr2[2:5]);
arr2[2:5] = 23;
# 隐式迭代
print(arr2);
print("-----------------------");

arrSlice = arr2[2:5];
arrSlice[:] = 10000;  # 全部赋为10000
print(arr2);
# 注意切片返回的数据是原始数组的视图而非拷贝
arrCopy = arr2[2:5].copy();
arrCopy[:] = 1234;
# 如果要拷贝，那么需要调用copy方法
print(arrCopy);
print(arr2);

print("-------------------------");

# 高维数组使用下标访问，得到的是低一级的数组；连续使用下标n次就得到低n级的数组
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
print(arr2D[1]);

print(arr2D[1][1]);
print(arr2D[1, 1]);
# 多次使用下标,也可以使用逗号分割

# 可以将标量和相同大小的数组赋给arr
# 使用下标访问返回的也是视图，而非拷贝

