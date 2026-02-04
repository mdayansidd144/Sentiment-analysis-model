from src.imdb_fetcher import fetch_movie_data
from src.movie_sentiment import analyze_movie
def analyze_movie_by_name(movie_name):
    data = fetch_movie_data(movie_name)
    if not data:
        return {"error": "Movie not found"}
    result = analyze_movie(data)
    # Final verdict
    if result["plot_sentiment"] == "Positive" and result["rating_sentiment"] == "Positive":
        verdict = "Highly Recommended 🎉"
    elif result["plot_sentiment"] == "Negative":
        verdict = "Poor Audience Response ⚠️"
    else:
        verdict = "Average Reception ⭐"
    result["verdict"] = verdict
    return result
