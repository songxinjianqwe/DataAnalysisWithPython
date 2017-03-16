from pandas import DataFrame, Series
import pandas as pd
import numpy as np

left = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
print(left)
#   key  value
# 0   a      0
# 1   b      1
# 2   a      2
# 3   a      3
# 4   b      4
# 5   c      5

right = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(right)
#    group_val
# a        3.5
# b        7.0

# 有时候，DataFrame的连接键位于其索引中。
# 在这种情况下，可以传入left_index=True或right_index=True（或两个都穿）以说明索引应该被用作连接键
# 注意，此时merge后中就不包含传入left_index/right_index的属性列了

result1 = pd.merge(left, right, left_on='key', right_index=True)
print(result1)
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0


# range()返回的是range object，而np.nrange()返回的是numpy.ndarray()
# range尽可用于迭代，而np.nrange作用远不止于此，它是一个序列，可被当做向量使用。
# 
# range()不支持步长为小数，np.arange()支持步长为小数

# 层次化的索引数据
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5)})
print(lefth)
#    data    key1  key2
# 0     0    Ohio  2000
# 1     1    Ohio  2001
# 2     2    Ohio  2002
# 3     3  Nevada  2001
# 4     4  Nevada  2002

righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])
print(righth)
#              event1  event2
# Nevada 2001       0       1
#        2000       2       3
# Ohio   2000       4       5
#        2000       6       7
#        2001       8       9
#        2002      10      11

result2 = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print(result2)
#    data    key1  key2  event1  event2
# 0     0    Ohio  2000       4       5
# 0     0    Ohio  2000       6       7
# 1     1    Ohio  2001       8       9
# 2     2    Ohio  2002      10      11
# 3     3  Nevada  2001       0       1

result3 = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
print(result3)
#    data    key1  key2  event1  event2
# 0   0.0    Ohio  2000     4.0     5.0
# 0   0.0    Ohio  2000     6.0     7.0
# 1   1.0    Ohio  2001     8.0     9.0
# 2   2.0    Ohio  2002    10.0    11.0
# 3   3.0  Nevada  2001     0.0     1.0
# 4   4.0  Nevada  2002     NaN     NaN
# 4   NaN  Nevada  2000     2.0     3.0

left2 = DataFrame([[1, 2], [3, 4], [5, 6]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
print(left2)
#    Ohio  Nevada
# a     1       2
# c     3       4
# e     5       6
right2 = DataFrame([[7, 8], [9, 10], [11, 12], [13, 14]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
print(right2)
#    Missouri  Alabama
# b         7        8
# c         9       10
# d        11       12
# e        13       14

result4 = pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
print(result4)
#    Ohio  Nevada  Missouri  Alabama
# a   1.0     2.0       NaN      NaN
# b   NaN     NaN       7.0      8.0
# c   3.0     4.0       9.0     10.0
# d   NaN     NaN      11.0     12.0
# e   5.0     6.0      13.0     14.0

# DataFrame还有一个join实例方法，它能更为方便地实现按索引合并。它还可用于合并多个带有相同或相似索引的DataFrame对象，
# 而不管它们之间有没有重叠的列。
print(left2.join(right2, how='outer'))
#    Ohio  Nevada  Missouri  Alabama
# a   1.0     2.0       NaN      NaN
# b   NaN     NaN       7.0      8.0
# c   3.0     4.0       9.0     10.0
# d   NaN     NaN      11.0     12.0
# e   5.0     6.0      13.0     14.0

# 对于简单的索引合并，你还可以向join传入一组DataFrame
another = DataFrame([[7, 8], [9, 10], [11, 12], [16, 17]], index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregen'])
print(left2.join([right2, another]))
#    Ohio  Nevada  Missouri  Alabama  New York  Oregen
# a     1       2       NaN      NaN         7       8
# c     3       4       9.0     10.0         9      10
# e     5       6      13.0     14.0        11      12


