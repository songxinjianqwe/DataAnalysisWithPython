import pandas as pd
from pandas import DataFrame, Series

# 逐块读取文本文件

pathEx6= "D:/py/DataAnalysis/pydata-book-master/ch06/ex6.csv"

frame = pd.read_csv(pathEx6)
# print(frame)
# 10000行

# 如果只想读取几行，通过nrows进行指定即可

frame2 = pd.read_csv(pathEx6, nrows=5)
print(frame2)
#         one       two     three      four key
# 0  0.467976 -0.038649 -0.295344 -1.824726   L
# 1 -0.358893  1.404453  0.704965 -0.200638   B
# 2 -0.501840  0.659254 -0.421691 -0.057688   G
# 3  0.204886  1.074134  1.388361 -0.982404   R
# 4  0.354628 -0.133116  0.283763 -0.837063   Q

# 要逐块读取文件，需要设置chunksize（行数）：
chunker = pd.read_csv(pathEx6, chunksize=1000)
# chunker 是一个TextParser对象，可以根据chunksize对文件进行逐块迭代
# 比如像将值计数到key列中

tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])
# E    368.0
# X    364.0
# L    346.0
# O    343.0
# Q    340.0
# M    338.0
# J    337.0
# F    335.0
# K    334.0
# H    330.0
# dtype: float64


