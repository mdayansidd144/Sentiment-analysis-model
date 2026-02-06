import pandas as pd
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASETS = {
    "Social Media": "social_media_opinions.csv",
    "Geopolitics": "geopolitics_opinions.csv",
    "Technology": "technology_reviews.csv"
}
def load_public_opinions(topic, limit=300):
    if topic not in DATASETS:
        return []
    path = os.path.join(BASE_DIR, "data", DATASETS[topic])
    if not os.path.exists(path):
        return []
    df = pd.read_csv(path)

    if "text" not in df.columns:
        return []
    return df["text"].dropna().head(limit).tolist()
