from pandas import DataFrame, Series
import numpy as np


# 重新调整某条轴上各级别的顺序，或根据指定级别上的值对数据进行排序
# swaplevel接受两个级别编号或名称，并返回了一个互换了级别的新对象，但数据不会发生变化
frame = DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame.swaplevel('key1', 'key2'))
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
# 2    a        3   4        5
# 1    b        6   7        8
# 2    b        9  10       11

# sortlevel 是根据单个级别中的值对数据进行排序，是稳定排序
# 交换级别时，常常也会用到sortlevel
# 参数从0开始，0表示最外层的索引
print(frame.sortlevel(1))
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
# b    1        6   7        8
# a    2        3   4        5
# b    2        9  10       11
# 先交换内外层索引，然后按新的外层索引排序
print(frame.swaplevel(0, 1).sortlevel(0))
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
#      b        6   7        8
# 2    a        3   4        5
#      b        9  10       11

