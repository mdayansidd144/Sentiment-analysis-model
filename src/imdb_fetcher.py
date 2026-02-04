import requests
API_KEY = "e595840e"
def fetch_movie_data(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "False":
        return None
    return {
        "title": data.get("Title"),
        "year": data.get("Year"),
        "genre": data.get("Genre"),
        "plot": data.get("Plot"),
        "rating": data.get("imdbRating"),
        "votes": data.get("imdbVotes")
    }
