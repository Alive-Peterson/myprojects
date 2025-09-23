#importing required modules
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from math import sqrt

#configuring paths
DATA_DIR = "ml-latest-small"
RATINGS_FILE = f"{DATA_DIR}/ratings.csv"
MOVIES_FILE = f"{DATA_DIR}/movies.csv"

#Loading Data
ratings = pd.read_csv(RATINGS_FILE)
movies = pd.read_csv(MOVIES_FILE)
print(f"ratings row:", len(ratings))
print(f"movies row:", len(movies))

#train test split
from sklearn.model_selection import train_test_split
train_ratings, test_ratings = train_test_split(ratings, test_size=0.2, random_state=42)

#creating user item matrix(train)
train_data = pd.merge(train_ratings, movies, on ='movieId', how ='left')
test_data = pd.merge(test_ratings, movies, on ='movieId', how ='left')

user_movie_train = train_data.pivot_table(index='userId', columns='movieId', values='rating')
user_movie_train_filled = user_movie_train.fillna(0)  # fill NaN with 0 for KNN

print("Train matrix shape:", user_movie_train.shape)

# Mean Clustering
user_means = user_movie_train.mean(axis=1)
normalized = user_movie_train.sub(user_means, axis=0).fillna(0)

#Fit KNN on users
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(normalized.values)

user_id_to_index = {user_id: idx for idx, user_id in enumerate(normalized.index)}
index_to_user_id = {idx: user_id for user_id, idx in user_id_to_index.items()}

#User-based CF prediction