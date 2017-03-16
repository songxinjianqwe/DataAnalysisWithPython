from pandas import Series, np

strings = Series(["aardvark", "artichoke", np.nan, "avocado"])
print(strings)
# 0     aardvark
# 1    artichoke
# 2          NaN
# 3      avocado
# dtype: object

print(strings.isnull())
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool

strings[0] = None
print(strings.isnull())

