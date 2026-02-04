# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.datasets import imdb
# from src.domain_classifier import detect_domain
# from src.model import build_model
# VOCAB_SIZE = 10000
# MAX_LEN = 150
# word_index=imdb.get_word_index()
# model = build_model()
# def safe_encode(text):
#     tokens = []
#     for w in text.lower().split():
#         idx = word_index.get(w, 2)
#         if idx < VOCAB_SIZE:         
#             tokens.append(idx)
#         else:
#             tokens.append(2)          
#     return tokens
# def predict_sentiment(text):
#     domain = detect_domain(text)
#     tokens = [word_index.get(w,2)for w in text.lower().split()]
#     padded = pad_sequences([tokens],maxlen=MAX_LEN)
#     prediction = model.predict(padded)
#     score = prediction.item()

#     return {
#         "domain": domain,
#         "sentiment": "Positive" if score > 0.5 else "",
#         "confidence":round(score,2)

#     }
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
from src.domain_classifier import detect_domain
from src.model import build_model

VOCAB_SIZE = 10000
MAX_LEN = 150
POSITIVE_STRONG = {"awesome", "excellent", "fantastic", "amazing", "outstanding"}
POSITIVE_MILD = {"good", "nice", "decent", "pleasant"}
NEGATIVE_STRONG = {"terrible", "awful", "horrible", "worst"}
NEGATIVE_MILD = {"bad", "poor", "boring", "disappointing"}
word_index = imdb.get_word_index()
model = build_model()
def safe_encode(text):
    tokens = []
    for w in text.lower().split():
        idx = word_index.get(w, 2)
        tokens.append(idx if idx < VOCAB_SIZE else 2)
    return tokens
def lexical_adjustment(text, score):
    words = set(text.lower().split())
    if words & POSITIVE_STRONG:
        score += 0.30
    elif words & NEGATIVE_STRONG:
        score -= 0.40
    elif words & POSITIVE_MILD:
        score += 0.10
    elif words & NEGATIVE_MILD:
        score -= 0.10
    return min(max(score, 0.0), 1.0)
def sentiment_label(score):
    if score < 0.15:
        return "very poor"
    elif score < 0.40:
        return "poor"
    elif score < 0.50:
        return "neutral"
    elif score < 0.60:
        return "decent"
    elif score < 0.75:
        return "good"
    elif score < 0.90:
        return "great"
    else:
        return "awesome"
def predict_sentiment(text):
    domain = detect_domain(text)

    encoded = safe_encode(text)
    padded = pad_sequences([encoded], maxlen=MAX_LEN)

    prediction = model.predict(padded)
    score = prediction.item()
    score = lexical_adjustment(text, score)
    label = sentiment_label(score)
    return {
        "domain": domain,
        "sentiment": label,
        "confidence": round(score, 3),
        "raw_score": round(score,2)
    }
