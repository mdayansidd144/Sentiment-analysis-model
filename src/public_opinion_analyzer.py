from src.predict import predict_sentiment
def analyze_public_opinion(texts):
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
#  ye hamare saare public opinions ko classify krenga
    for t in texts:
        result = predict_sentiment(t)
        label = result["sentiment"]
        summary[label] += 1
        timeline.append(result["confidence"])
    total = sum(summary.values()) or 1
    percentages = {k: round(v / total * 100, 2) for k, v in summary.items()}
    return percentages, timeline
