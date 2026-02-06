from src.news_fetcher import fetch_news_texts
from src.predict import predict_sentiment
def analyze_news_topic(topic):
    texts = fetch_news_texts(topic)
    if not texts:
        return {"error": "No news data found"}
    summary = {}
    timeline = []
    for t in texts:
        result = predict_sentiment(t)
        label = result["sentiment"]
        summary[label] = summary.get(label, 0) + 1
        timeline.append(result["confidence"])
    return {
        "topic": topic,
        "summary": summary,
        "timeline": timeline,
        "count": len(texts)
    }
