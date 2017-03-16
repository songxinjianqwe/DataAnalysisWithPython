from pandas import DataFrame, Series
import pandas as pd
# HDF5 能实现高效读写硬盘上的二进制数据
# 很多语言都有HDF5的接口
# HDF：Hierarchical data format
# 可以高效率地分块读写
path = "D:/py/DataAnalysis/pydata-book-master/ch06/ex1.csv"
frame = pd.read_csv(path)

# pandas有一个最小化的类似于字典的HDFStore类，它通过pyTables存储pandas对象
store = pd.HDFStore("mydata.h5")
store['obj1'] = frame
store['obj1_col'] = frame['a']

print(store)
# <class 'pandas.io.pytables.HDFStore'>
# File path: mydata.h5
# /obj1                frame        (shape->[3,5])
# /obj1_col            series       (shape->[3])  
# 可以像字典一样的方式进行存取
print(store['obj1'])
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo



