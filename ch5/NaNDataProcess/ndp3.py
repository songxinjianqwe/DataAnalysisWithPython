from pandas import Series, np, DataFrame

frame = DataFrame(np.random.randn(5, 3))
frame.ix[:3, 1] = np.nan
frame.ix[:1, 2] = np.nan
print(frame)
#           0         1         2
# 0 -0.951174       NaN       NaN
# 1  0.199047       NaN       NaN
# 2 -0.556298       NaN  2.338692
# 3  1.288069       NaN  0.427623
# 4  1.079251  0.525899 -1.430305
print(frame.fillna(0))
#           0         1         2
# 0 -0.951174  0.000000  0.000000
# 1  0.199047  0.000000  0.000000
# 2 -0.556298  0.000000  2.338692
# 3  1.288069  0.000000  0.427623
# 4  1.079251  0.525899 -1.430305

# 如果是通过一个字典调用fillna，就可以实现对不同的列填充不同的值
print(frame.fillna({1: 0.5, 2: -1}))
#           0         1         2
# 0  0.654535  0.500000 -1.000000
# 1 -0.544232  0.500000 -1.000000
# 2 -1.314791  0.500000  0.083983
# 3 -0.741554  0.500000 -0.397393
# 4  0.458317  0.574526  1.487822


# fillna默认是返回新的对象，但也可以对现有对象就地修改
# frame.fillna(0, inplace=True)
print(frame)
# 对reindex 有效的那些插值方法也可以用于fillna
# 比如ffill bfill
#           0         1         2
# 0  0.347392       NaN       NaN
# 1 -0.137815       NaN       NaN
# 2  0.401997       NaN  0.726207
# 3  0.356190       NaN -1.599159
# 4  1.765341  2.770447 -1.257416
print(frame.fillna(method="bfill"))
#           0         1         2
# 0  0.347392  2.770447  0.726207
# 1 -0.137815  2.770447  0.726207
# 2  0.401997  2.770447  0.726207
# 3  0.356190  2.770447 -1.599159
# 4  1.765341  2.770447 -1.257416
