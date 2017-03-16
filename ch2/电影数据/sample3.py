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
ratingByTitle = data.groupby("title").size();
validTitles = ratingByTitle.index[ratingByTitle >= 250];
meanRatings= meanRatings.ix[validTitles];
# 这里的是去掉了评分数据<250条后的大表
# -----------------------------------------------------------------------------------------------------------

meanRatings["diff"] = meanRatings["M"] - meanRatings["F"];
# 添加一列，表示是男女评分的分歧
sortedByDiff = meanRatings.sort_values(by="diff",ascending=True);
# 按照分歧的分数升序排序,得到分歧最大且女性更喜欢的电影
print(sortedByDiff[:5]);
print(sortedByDiff[::-1][:5]);
# 反转之后得到分歧最大且男性更喜欢的电影


