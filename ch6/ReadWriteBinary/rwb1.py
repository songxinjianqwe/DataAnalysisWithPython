from pandas import DataFrame, Series
import pandas as pd
import pickle
path = "D:/py/DataAnalysis/pydata-book-master/ch06/ex1.csv"

# 内置的pickle序列化
frame = pd.read_csv(path)
print(frame)
pickle.dump(frame, open("frame_pickle", "wb"))
frame2 = pickle.load(open("frame_pickle", "rb"))
print(frame2)
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo



