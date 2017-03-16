from pandas import DataFrame
import numpy as np

frame = DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11
# 许多对DataFrame和Series的描述和汇总统计中都有一个level选项，它用于指定在某条轴上求和的级别。
# 可以根据行或列上的级别来进行求和
print(frame.sum(level='key2'))
# state  Ohio     Colorado
# color Green Red    Green
# key2
# 1         6   8       10
# 2        12  14       16

# 可以添加一个参数axis，如果为0，则表示按索引统计；如果为1，则表示按属性统计
print(frame.sum(level='color', axis=1))
# color      Green  Red
# key1 key2
# a    1         2    1
#      2         8    4
# b    1        14    7
#      2        20   10

