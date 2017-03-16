from pandas import DataFrame, Series
import pandas as pd

# pandas 的merge方法 可以根据一个或多个键将不同DataFrame的行连接起来
# concat可以沿着一条轴将多个对象堆叠到一起
# combine_first 类似于数据库的外连接

frame1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
frame2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
print(frame1)
#    data1 key
# 0      0    b
# 1      1    b
# 2      2    a
# 3      3    c
# 4      4    a
# 5      5    a
# 6      6    b

print(frame2)
#    data2 key
# 0      0    a
# 1      1    b
# 2      2    d
result = pd.merge(frame1, frame2)
print(result)
#    data1 key  data2
# 0      0   b      1
# 1      1   b      1
# 2      6   b      1
# 3      2   a      0
# 4      4   a      0
# 5      5   a      0

# 如果没有指定用哪个列进行连接，就会将重叠列的列名当做键。也可以显式指定下。
result2 = pd.merge(frame1, frame2, on='key')
# 如果两个对象的列名不同，也可以分组进行指定。
frame3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
frame4 = DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
result3 = pd.merge(frame3, frame4, left_on='lkey', right_on='rkey')
print(result3)
#    data1 lkey  data2 rkey
# 0      0    b      1    b
# 1      1    b      1    b
# 2      6    b      1    b
# 3      2    a      0    a
# 4      4    a      0    a
# 5      5    a      0    a

# 默认情况下，merge做的是内连接
# 可以指定左外连接，右外连接，外连接

result4 = pd.merge(frame1, frame2, how='outer')
print(result4)
#    data1 key  data2
# 0    0.0   b    1.0
# 1    1.0   b    1.0
# 2    6.0   b    1.0
# 3    2.0   a    0.0
# 4    4.0   a    0.0
# 5    5.0   a    0.0
# 6    3.0   c    NaN
# 7    NaN   d    2.0

frame5 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data2': range(6)})
print(frame5)
#    data2 key
# 0      0   b
# 1      1   b
# 2      2   a
# 3      3   c
# 4      4   a
# 5      5   b

frame6 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
print(frame6)
#    data2 key
# 0      0   a
# 1      1   b
# 2      2   a
# 3      3   b
# 4      4   d

result5 = pd.merge(frame5, frame6, on='key', how='left')
print(result5)
#     data2_x key  data2_y
# 0         0   b      1.0
# 1         0   b      3.0
# 2         1   b      1.0
# 3         1   b      3.0
# 4         2   a      0.0
# 5         2   a      2.0
# 6         3   c      NaN
# 7         4   a      0.0
# 8         4   a      2.0
# 9         5   b      1.0
# 10        5   b      3.0

# 多对多连接产生的是行的笛卡尔积
result6 = pd.merge(frame5, frame6, on='key', how='inner')
print(result6)
#    data2_x key  data2_y
# 0        0   b        1
# 1        0   b        3
# 2        1   b        1
# 3        1   b        3
# 4        5   b        1
# 5        5   b        3
# 6        2   a        0
# 7        2   a        2
# 8        4   a        0
# 9        4   a        2


# 要根据多个键进行合并，传入一个由列名组成的列表即可
frame7 = DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})
print(frame7)
#   key1 key2  lval
# 0  foo  one     1
# 1  foo  two     2
# 2  bar  one     3
frame8 = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
print(frame8)
#   key1 key2  rval
# 0  foo  one     4
# 1  foo  one     5
# 2  bar  one     6
# 3  bar  two     7
result7 = pd.merge(frame7, frame8, on = ['key1', 'key2'], how='outer')
print(result7)
#   key1 key2  lval  rval
# 0  foo  one   1.0   4.0
# 1  foo  one   1.0   5.0
# 2  foo  two   2.0   NaN
# 3  bar  one   3.0   6.0
# 4  bar  two   NaN   7.0

# 进行列列连接时，DataFrame对象中的索引会被丢弃
# 重复列名：使用suffixes选项，用于指定附加到左右两个DataFrame对象的重叠列名的字符串
result8 = pd.merge(frame7, frame8,on='key1', suffixes=['_left', '_right'])
print(result8)
#   key1 key2_left  lval key2_right  rval
# 0  foo       one     1        one     4
# 1  foo       one     1        one     5
# 2  foo       two     2        one     4
# 3  foo       two     2        one     5
# 4  bar       one     3        one     6
# 5  bar       one     3        two     7

