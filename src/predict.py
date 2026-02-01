from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
from src.domain_classifier import detect_domain
from src.model import build_model

word_index=imdb.get_word_index()
model = build_model()

def predict_sentiment(text):
    domain = detect_domain(text)
    tokens = [word_index.get(w,2)for w in text.lower().split()]
    padded = pad_sequences([tokens],maxlen=150)
    prediction = model.predict(padded)
    score = prediction.item()

    return {
        # "domain": domain,
        "sentiment":"positive" if score>0.5 else"negative",
        "confidence":round(score,2)

    }