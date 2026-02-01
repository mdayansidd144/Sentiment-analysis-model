from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment")
emotion_model = pipeline("text-classification",
    model= "j-hartmann/emotion-english-distilroberta-base",
    top_k = None)
def analyze_sentiment(text):
    sentiment = sentiment_model(text)[0]
    emotion = emotion_model(text)[0]
    return{
        "sentiment":sentiment["label"],
        "confidence":round(sentiment["score"],3),
        "emotion":emotion
    }