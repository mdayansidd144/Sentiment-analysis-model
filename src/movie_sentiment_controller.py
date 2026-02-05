from src.imdb_fetcher import fetch_movie_data
from src.review_loader import load_reviews
from src.review_sentiment_engine import analyze_reviews
from src.predict import predict_sentiment
def analyze_imdb_movie(movie_name):
    meta = fetch_movie_data(movie_name)
    if not meta:
        return {"error": "Movie not found"}

    plot_sentiment = predict_sentiment(meta["plot"])
    reviews = load_reviews(movie_name)

    review_summary, timeline = analyze_reviews(reviews) if reviews else ({}, [])

    return {
        "meta": meta,
        "plot_sentiment": plot_sentiment,
        "review_summary": review_summary,
        "timeline": timeline
    }
