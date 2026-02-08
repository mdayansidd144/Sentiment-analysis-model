import requests
import os
from dotenv import load_dotenv
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  
def fetch_news_texts(query, limit=20):
    if not NEWS_API_KEY:
        print("❌ NEWS_API_KEY missing")
        return []
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "pageSize": limit,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    texts = []
    for a in articles:
        if a.get("title"):
            texts.append(a["title"])
        if a.get("description"):
            texts.append(a["description"])
    return texts
