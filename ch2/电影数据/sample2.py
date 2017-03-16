import pandas as pd;

base = "D:/py/DataAnalysis/pydata-book-master/ch02/movielens/";
userFields = ["user_id", "gender", "age", "occupation", "zip"];
users = pd.read_table(base + "users.dat", sep="::", header=None, names=userFields,engine="python");

ratingFields = ["user_id", "movie_id", "rating", "timestamp"];
ratings = pd.read_table(base + "ratings.dat", sep="::", header=None, names=ratingFields,engine="python");

movieFields = ["movie_id","title","genres"];
movies = pd.read_table(base+"movies.dat",sep="::",header=None,names=movieFields,engine="python");
data = pd.merge(pd.merge(ratings,users),movies);
meanRatings = pd.pivot_table(data=data,values="rating",index="title",columns="gender",aggfunc="mean");
# ------------------------------------------------------------------------------------------------------------
ratingByTitle = data.groupby("title").size();
# 先按title分组，调用size()可以得到一个含有各电影分组大小的Series对象
# print(ratingByTitle[:5]);

validTitles = ratingByTitle.index[ratingByTitle >= 250];
# 过滤掉评分数据不足250条的记录，隐式迭代，返回的是Index，类似于列表
# print(validTitles);

meanRatings= meanRatings.ix[validTitles];
# 在连接后的大表中过滤掉评分数据不足250的记录
# print(meanRatings);

topFemaleRatings = meanRatings.sort_values(by="F",ascending=False);
# 按照女性性别降序排序
print(topFemaleRatings[:10]);

