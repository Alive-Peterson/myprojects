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

