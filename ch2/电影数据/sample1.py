import pandas as pd;

base = "D:/py/DataAnalysis/pydata-book-master/ch02/movielens/";
# dat格式不是一种标准格式，通常是数据分析中的一种文件格式，用于存储数据
# read_table得到的数据非常类似于数据库中的数据表
userFields = ["user_id", "gender", "age", "occupation", "zip"];
users = pd.read_table(base + "users.dat", sep="::", header=None, names=userFields,engine="python");

ratingFields = ["user_id", "movie_id", "rating", "timestamp"];
ratings = pd.read_table(base + "ratings.dat", sep="::", header=None, names=ratingFields,engine="python");

movieFields = ["movie_id","title","genres"];
movies = pd.read_table(base+"movies.dat",sep="::",header=None,names=movieFields,engine="python");
#取出数据，形成数据表，放入内存中
# print(users[:5]);
# print(ratings[:5]);
# print(movies[:5]);


data = pd.merge(pd.merge(ratings,users),movies);#merge返回的是DataFrame，将多张表按照相同的属性连接起来，类似于SQL中的join
# print(data);
# print(data.ix[0]);#取出索引为0的记录
meanRatings = pd.pivot_table(data=data,values="rating",index="title",columns="gender",aggfunc="mean");
# values是属性值，这里是评分；title是行标，为电影名；columns是列标，为性别(的所有取值)；计算values的平均值
# 实际上就是拿到不同性别对于每部电影的评分均值
# 返回值仍为DataFrame
print(meanRatings[:5]);






