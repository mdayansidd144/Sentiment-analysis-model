from src.public_opinion_loader import load_public_opinions
from src.public_opinion_analyzer import analyze_public_opinion
def analyze_topic(topic):
    texts = load_public_opinions(topic)
    if not texts:
        return {"error": "No data available for this topic"}
    summary, timeline = analyze_public_opinion(texts)
    return {
        "topic": topic,
        "summary": summary,
        "timeline": timeline
    }
# overall hamare sentiments ko accordingly review krenga