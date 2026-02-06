from src.youtube_fetcher import fetch_youtube_comments
from src.predict import predict_sentiment
def analyze_youtube_video(video_id):
    try:
        texts = fetch_youtube_comments(video_id)
    except RuntimeError as e:
        return {"error": str(e)}

    if not texts:
        return {"error": "No comments found"}
    summary = {}
    timeline = []
    for t in texts:
        result = predict_sentiment(t)
        label = result["sentiment"]
        summary[label] = summary.get(label, 0) + 1
        timeline.append(result["confidence"])
    return {
        "video_id": video_id,
        "summary": summary,
        "timeline": timeline,
        "count": len(texts)
    }
