from src.predict import predict_sentiment
def analyze_reviews(reviews):
    timeline = []
    summary = {
        "very poor": 0,
        "poor": 0,
        "neutral": 0,
        "decent": 0,
        "good": 0,
        "great": 0,
        "awesome": 0
    }
    for r in reviews:
        result = predict_sentiment(r)
        label = result["sentiment"]
        summary[label] += 1
        timeline.append(result["confidence"])
    total = sum(summary.values())
    percentages = {k: round(v / total * 100, 2) for k, v in summary.items()}
    return percentages, timeline
