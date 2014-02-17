import pandas as pd

os.chdir('/home/brad/Desktop/pydata-book/ch02/movielens/')

unames = ['user_id','gender','age','ocupation','zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)

rnames = ['user_id','movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)

users[:5]
ratings[:5]
movies[:5]

# to start the analysis we will first merge the dataframes
data = pd.merge(pd.merge(ratings, users), movies)
data  # to check the results of the merge
data.ix[0]

# we will use aggregate to do some simple grouping eval by gender
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
# we will view a subset of only those movies which recieved at least 250 rates
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]
active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles[:10]
# This new active_titles variable can be used as the index for selecting rows from mean_ratings
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings
# to view the top films amoung female viewers we will sort by the 'F' column
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]

# Now we will try to find which moviews were most highly favored by women
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sort_by_diff = mean_ratings.sort_index(by='diff')
sort_by_diff[:15]
# We can also check in reverese order
sort_by_diff[::-1][:15]
sort_by_diff[-15:][::-1]   # The [::-1] is an example of extendd slicing

# Now we want to find the most disagreement from all the viewers
rating_std_by_title = data.groupby('title')['rating'].std()
# But we still only want from the active titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
rating_std_by_title.order(ascending=False)[:10]









