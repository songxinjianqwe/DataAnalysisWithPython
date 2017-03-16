from pandas import Series, np, DataFrame

data = Series([1, np.nan, 3.5, np.nan, 7])
print(data)
# 去掉空值
print(data.dropna())

# 或者这样去掉空值
print(data.notnull())
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool
print(data[data.notnull()])
# 0    1.0
# 2    3.5
# 4    7.0
# dtype: float64

# dropna默认会丢弃任何含有缺失值的行
frame = DataFrame([[1, 6.5, 3], [1, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3]])
print(frame)
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  6.5  3.0
cleaned = frame.dropna()
print(cleaned)
#      0    1    2
# 0  1.0  6.5  3.0

# 传入how='all' 将只丢弃全为nan的行
print(frame.dropna(axis=0, how='all'))
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 3  NaN  6.5  3.0
frame["3"] = np.nan
print(frame)
#      0    1    2   3
# 0  1.0  6.5  3.0 NaN
# 1  1.0  NaN  NaN NaN
# 2  NaN  NaN  NaN NaN
# 3  NaN  6.5  3.0 NaN

# axis=1 时 会丢弃全为nan的列
print(frame.dropna(axis=1, how='all'))
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  6.5  3.0

# thresh: int value : require that many non-NA values
frame2 = DataFrame(np.random.randn(7, 3))
print(frame2)
#           0         1         2
# 0 -0.555630 -0.455073  0.930049
# 1  1.010013  1.051915  2.063610
# 2  1.490995  0.310320  1.453123
# 3  2.473785  0.230897 -0.262998
# 4 -0.144009 -1.368337  1.120999
# 5 -0.478260  1.560264 -0.926439
# 6 -0.292404  1.534631 -0.434683
frame2.ix[:4, 1] = np.nan
frame2.ix[:2, 2] = np.nan
print(frame2)
#           0         1         2
# 0 -0.555630       NaN       NaN
# 1  1.010013       NaN       NaN
# 2  1.490995       NaN       NaN
# 3  2.473785       NaN -0.262998
# 4 -0.144009       NaN  1.120999
# 5 -0.478260  1.560264 -0.926439
# 6 -0.292404  1.534631 -0.434683
# 要求每行要有三个不是nan的数据才能留下，其他的行都被筛掉了
print(frame2.dropna(thresh=3))
#           0         1         2
# 5 -0.478260  1.560264 -0.926439
# 6 -0.292404  1.534631 -0.434683
