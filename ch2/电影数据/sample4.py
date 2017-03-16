import pandas as pd;

base = "D:/py/DataAnalysis/pydata-book-master/ch02/movielens/";
userFields = ["user_id", "gender", "age", "occupation", "zip"];
users = pd.read_table(base + "users.dat", sep="::", header=None, names=userFields,engine="python");

ratingFields = ["user_id", "movie_id", "rating", "timestamp"];
ratings = pd.read_table(base + "ratings.dat", sep="::", header=None, names=ratingFields,engine="python");

movieFields = ["movie_id","title","genres"];
movies = pd.read_table(base+"movies.dat",sep="::",header=None,names=movieFields,engine="python");
data = pd.merge(pd.merge(ratings,users),movies);
ratingByTitle = data.groupby("title").size();
validTitles = ratingByTitle.index[ratingByTitle >= 250];
# -----------------------------------------------------------------------------------------------
ratingStdByTitle = data.groupby("title")["rating"].std();
# 按照电影名分组，取出评分这一列，然后计算标准差（差异），目的是得到观众们对于电影评分分歧最大的电影们
ratingStdByTitle = ratingStdByTitle.ix[validTitles]; # 筛选
print(ratingStdByTitle.sort_values(ascending=False)[:10]);





