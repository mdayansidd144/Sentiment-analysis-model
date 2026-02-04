# from src.predict import predict_sentiment
# def analyze_movie(movie_data):
#     plot = movie_data["plot"]
#     rating = float(movie_data["rating"]) if movie_data["rating"] != "N/A" else 0
#     sentiment = predict_sentiment(plot)

#     # Rating-based on the given sentiments
#     if rating >= 7:
#         rating_sentiment = "Positive"
#     elif rating <=4 :
#         rating_sentiment = "Negative"
#     else:
#         rating_sentiment = "Neutral"
#     return {
#         "movie": movie_data["title"],
#         "year": movie_data["year"],
#         "genre": movie_data["genre"],
#         "plot_sentiment": sentiment["sentiment"],
#         "confidence": sentiment["confidence"],
#         "rating": rating,
#         "rating_sentiment": rating_sentiment
#     }
from src.imdb_fetcher import fetch_movie_data
from src.review_loader import load_reviews
from src.review_sentiment_engine import analyze_reviews
from src.predict import predict_sentiment

def analyze_imdb_movie(movie_name):
    meta = fetch_movie_data(movie_name)
    if not meta:
        return {"error": "Movie not found"}
    plot_result = predict_sentiment(meta["plot"])
    reviews = load_reviews(movie_name)
    review_summary, timeline = analyze_reviews(reviews)
    return {
        "meta": meta,
        "plot_sentiment": plot_result,
        "review_summary": review_summary,
        "timeline": timeline
    }
