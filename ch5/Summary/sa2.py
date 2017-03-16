from pandas import Series, DataFrame;
import pandas as pd;
import numpy as np;
import pandas_datareader.data as web;
# 有些汇总统计，比如相关系数和协方差，是通过参数对计算出来的。

allData = {};
for ticket in ["AAPL","IBM","MSFT","GOOG"]:
    allData[ticket] - web.get_data_yahoo(ticket,'1/1/2000','1/1/2010');
price = DataFrame({tic:data["Adj Close"] for tic,data in allData.items()});
volumn = DataFrame({tic:data["Volumn"] for tic,data in allData.items()});
# 计算百分比变化
results = price.pct_change();
# 返回MSFT和IBM之间的相关系数
print(results.MSFT.corr(results.IBM));
# 返回MSFT和IBM之间的协方差
print(results.MSFT.cov(results.IBM));

# 以DataFrame的形式返回完整的相关系数矩阵
print(results.corr());
# 以DataFrame的形式返回完整的协方差矩阵
print(results.cov());

# 利用DataFrame的corrwith方法，你可以计算其列或行跟另一个Series或DataFrame之间的相关系数
# 传入一个Series将会返回一个相关系数Series，针对各列计算
print(results.corrwith(results.IBM));
print(results.covwith(results.IBM));



