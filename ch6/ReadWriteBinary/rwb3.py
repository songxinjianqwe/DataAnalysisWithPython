import pandas as pd
# 读取excel文件
xls_file = pd.ExcelFile('Whereabouts.xlsx')
table = xls_file.parse("Sheet1")
print(table)

