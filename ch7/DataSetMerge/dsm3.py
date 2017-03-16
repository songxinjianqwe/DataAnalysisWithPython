from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# 另一种数据合并运算也被称作连接、绑定或堆叠。
# Numpy有一个用于合并原始Numpy数组的concatenation函数
arr = np.arange(12).reshape((3, 4))
print(arr)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# 横向连接起来
print(np.concatenate([arr, arr], axis=1))
# [[ 0  1  2  3  0  1  2  3]
#  [ 4  5  6  7  4  5  6  7]
#  [ 8  9 10 11  8  9 10 11]]

# 纵向连接
print(np.concatenate([arr, arr], axis=0))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 对于Series和DataFrame，带有标签的列能够进一步推广数据的连接运算
