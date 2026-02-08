import pandas as pd
import os
from src.news_fetcher import fetch_news_texts
TOPIC_QUERY_MAP = {
    "Social Media": "social media public opinion",
    "Geopolitics": "global geopolitics international relations",
    "Technology": "technology innovation AI",
    "Sports": "sports fans reactions"
}
def load_public_opinions(topic, limit=100):
    topic = topic.strip().title()
    query = TOPIC_QUERY_MAP.get(topic)
    if not query:
        print("❌ Topic not mapped:", topic)
        return []
    print("🟢 Fetching public opinion for:", query)
    texts = fetch_news_texts(query, limit=limit)
    print("🟢 Texts fetched:", len(texts))
    return texts
