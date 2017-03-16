# coding=utf-8

import numpy as np;

arr = np.random.randn(5, 4);
print(arr);
print(arr.mean());
print(np.mean(arr));
# 求数组的均值，以上两种方式均可以
print(arr.sum());

# mean和sum这类的函数可以接受一个axis参数（用于计算该轴向上的统计值），最终结果是降一维的数组
result = arr.mean(axis=1);
# result[0] 是arr[0]的平均值；result[1] 是arr[1]的平均值
print(result);
result2 = arr.sum(axis=1);
# result[0] 是arr[0]的和；result[1] 是arr[1]的和
print(result2);
print();


# cumsum cumprod 是所有元素的累计和、累计积
# 0代表列的计算，1代表行的计算，即对列和行分别累积求和、 积。
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
res = arr.cumsum(0);
res2 = arr.cumsum(1);
print(res);
print(res2);
# 0：是将同一列上的上面的元素的和+当前值
# res[i][j] = sum(res[0~(i-1)][j]) + res[i][j]
# 1：是将同一行上的左侧的元素的和+当前值
# res[i][j] = sum(res[i][0~(j-1)]) + res[i][j]
print();

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
res = arr.cumprod(0);
res2 = arr.cumprod(1);
print(res);
print(res2);
