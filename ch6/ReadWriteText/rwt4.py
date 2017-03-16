import csv

# 手工处理分隔符格式
pathEx7 = "D:/py/DataAnalysis/pydata-book-master/ch06/ex7.csv"
# 文件内容：
# "a","b","c"
# "1","2","3"
# "1","2","3","4"

file = open(pathEx7)
reader = csv.reader(file)

# reader进行每次迭代都会为每行产生一个列表，并移除了所有的引号

for line in reader:
    print(line)
# ['a', 'b', 'c']
# ['1', '2', '3']
# ['1', '2', '3', '4']

lines = list(csv.reader(open(pathEx7)))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)
# {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# xyz = zip(x, y, z)
# u = zip(*xyz)
# [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# 一般认为这是一个unzip的过程，它的运行机制是这样的：
# 在运行zip(*xyz)之前，xyz的值是：[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# 那么，zip(*xyz) 等价于 zip((1, 4, 7), (2, 5, 8), (3, 6, 9))
# 所以，运行结果是：[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
