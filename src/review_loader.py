import pandas as pd
def load_reviews(movie_name, path="data/imdb_reviews.csv", limit=300):
    df = pd.read_csv(path)
    movie_df = df[df["movie"].str.contains(movie_name, case=False)]
    return movie_df["review"].dropna().head(limit).tolist()
