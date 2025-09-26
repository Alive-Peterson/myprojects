# 🎥 Movie Recommender System (User-Based Collaborative Filtering)

This project implements a **movie recommendation system** using **user-based collaborative filtering** with **K-Nearest Neighbors (KNN)**.  
It uses the **MovieLens dataset** to predict ratings and generate personalized movie recommendations.

---

## 📌 Features
- Builds a **User-Movie Matrix** from MovieLens ratings
- Normalizes ratings by subtracting user means
- Uses **cosine similarity with KNN** to find similar users
- Predicts ratings for unseen movies
- Evaluates performance using **RMSE (Root Mean Square Error)**
- Provides **Top-N recommendations** for any user

---

## 📂 Dataset
This project uses the [MovieLens Dataset (small version)](https://grouplens.org/datasets/movielens/).  
- `ratings.csv` → contains user ratings for movies  
- `movies.csv` → contains movie metadata (titles, genres)

Extract it into a folder named:
ml-latest-small/
├── ratings.csv
└── movies.csv

yaml
Copy code

---

## ⚙️ Installation

1. Clone this repository or copy the script.
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn
Download and extract the MovieLens small dataset into the project folder.

## ▶️ How to Run
Run the script:

bash
Copy code
python recommender.py
It will:

Load dataset (ratings.csv, movies.csv)

Train the KNN model

Compute RMSE on the test set

Print top-10 movie recommendations for a given user

## 🔢 Sample Output
Example console output:

```yaml
ratings row: 100836
movies row: 9742
Train matrix shape: (610, 9066)

RMSE on test set: 0.8942, Predictions made: 498, Skipped: 2

Top-10 recommendations for user 1:
Star Wars: Episode IV - A New Hope (1977) (pred 4.78)
The Empire Strikes Back (1980) (pred 4.65)
Return of the Jedi (1983) (pred 4.59)
```

## 🧠 Algorithm Overview
Create User-Movie Matrix (users as rows, movies as columns).

Normalize ratings by subtracting user averages.

Use KNN with cosine similarity to find nearest neighbors.

Predict ratings:

Weighted average of neighbor deviations from their means.

Recommend Top-N unrated movies with the highest predicted ratings.

## 📈 Evaluation
Metric: Root Mean Square Error (RMSE)

RMSE ≈ 0.89 (on MovieLens small dataset)

## 🛠️ Customization
Change k (number of neighbors) in predict_rating_user_based for different similarity strength.

Adjust n_recs in top_n_recommendations_for_user to control number of recommendations.

Replace MovieLens with your own dataset (must follow similar structure).

## 👤 Author
Alive Peterson
GitHub: @Alive-Peterson

