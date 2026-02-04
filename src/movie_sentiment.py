from src.predict import predict_sentiment
def analyze_movie(movie_data):
    plot = movie_data["plot"]
    rating = float(movie_data["rating"]) if movie_data["rating"] != "N/A" else 0
    sentiment = predict_sentiment(plot)

    # Rating-based on the given sentiments
    if rating >= 7:
        rating_sentiment = "Positive"
    elif rating >= 5:
        rating_sentiment = "Neutral"
    else:
        rating_sentiment = "Negative"
    return {
        "movie": movie_data["title"],
        "year": movie_data["year"],
        "genre": movie_data["genre"],
        "plot_sentiment": sentiment["sentiment"],
        "confidence": sentiment["confidence"],
        "rating": rating,
        "rating_sentiment": rating_sentiment
    }
