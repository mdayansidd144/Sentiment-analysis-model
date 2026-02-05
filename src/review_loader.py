# import pandas as pd
# def load_reviews(movie_name, path="data/imdb_reviews.csv", limit=300):
#     df = pd.read_csv(path)
#     movie_df = df[df["movie"].str.contains(movie_name, case=False)]
#     return movie_df["review"].dropna().head(limit).tolist()
# import pandas as pd
# import os
# # Absolute path to project
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# DATA_PATH = os.path.join(BASE_DIR, "data", "imdb_reviews.csv")

# def load_reviews(movie_name, limit=300):
#     if not os.path.exists(DATA_PATH):
#         raise FileNotFoundError(
#             f"IMDb reviews file not found.\nExpected at: {DATA_PATH}"
#         )

#     df = pd.read_csv(DATA_PATH)

#     # Safety checks
#     if "movie" not in df.columns or "review" not in df.columns:
#         raise ValueError("CSV must contain 'movie' and 'review' columns")

#     filtered = df[df["movie"].str.contains(movie_name, case=False, na=False)]
#     return filtered["review"].dropna().head(limit).tolist()
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "data", "imdb_reviews.csv")

def load_reviews(movie_name, limit=300):
    if not os.path.exists(DATA_PATH):
        return []

    df = pd.read_csv(DATA_PATH)

    if "movie" not in df.columns or "review" not in df.columns:
        return []

    filtered = df[df["movie"].str.contains(movie_name, case=False, na=False)]
    return filtered["review"].dropna().head(limit).tolist()
