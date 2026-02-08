from src.predict import predict_sentiment
def analyze_reviews(reviews):
    summary = {
        "very poor": 0,
        "poor": 0,
        "neutral": 0,
        "decent": 0,
        "good": 0,
        "great": 0,
        "awesome": 0
    }
    timeline = []
    for review in reviews:
        result = predict_sentiment(review)
        label = result["sentiment"]
        summary[label] += 1
        timeline.append(result["confidence"])
    total = sum(summary.values()) or 1
    percentages = {k: round(v / total * 100, 2)for k,v in summary.items()}
    return percentages, timeline
