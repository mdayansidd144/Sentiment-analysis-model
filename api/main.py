import sys
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_sentiment
from src.movie_sentiment_controller import analyze_imdb_movie
from src.public_opinion_controller import analyze_topic
from src.news_sentiment_controller import analyze_news_topic
from src.youtube_sentiment_controller import analyze_youtube_video   # ✅ NEW
app = FastAPI(
    title="Sentiment Intelligence API",
    description="Multi-domain sentiment analysis for text, movies, news, public opinion, and YouTube comments",
    version="1.1"
)
class TextRequest(BaseModel):
    text: str

class MovieRequest(BaseModel):
    movie_name: str

class TopicRequest(BaseModel):
    topic: str

class YouTubeRequest(BaseModel):
    video_id: str   # ✅ NEW
@app.get("/")
def health_check():
    return {
        "status": "Sentiment Intelligence API running",
        "services": [
            "Text Sentiment",
            "IMDb Movie Sentiment",
            "Public Opinion",
            "News Sentiment",
            "YouTube Comment Sentiment"
        ]
    }
@app.post("/analyze/text")
def analyze_text(req: TextRequest):
    return predict_sentiment(req.text)
@app.post("/analyze/movie")
def analyze_movie(req: MovieRequest):
    return analyze_imdb_movie(req.movie_name)
@app.post("/analyze/public-opinion")
def analyze_public_opinion(req: TopicRequest):
    return analyze_topic(req.topic)
@app.post("/analyze/news")
def analyze_news(req: TopicRequest):
    return analyze_news_topic(req.topic)
@app.post("/analyze/youtube")
def analyze_youtube(req: YouTubeRequest):
    return analyze_youtube_video(req.video_id)
