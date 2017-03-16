import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# pandas 最重要的一个功能是，它可以对不同索引的对象进行算术运算。在将对象相加时，如果存在不同的索引，则结果的索引就是该索引对的并集。

s1 = Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])
print(s1 + s2)

frame1 = DataFrame(np.arange(9).reshape((3, 3)), columns=list("bcd"), index=["Ohio", "Texas", "Colorado"])
print(frame1)
frame2 = DataFrame(np.arange(12).reshape((4, 3)), columns=list("bde"), index=["Utah", "Ohio", "Texas", "Oregen"])
print(frame2)
print(frame1 + frame2)
# 对齐会同时发生在行和列上
# columns = list("qwertyu")
