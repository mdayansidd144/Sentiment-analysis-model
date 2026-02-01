from src.transformer_model import analyze_text
from src.language_detector import detect_language
def smart_analyze(text):
    lang = detect_language(text)
    result = analyze_text(text)
    
    return{
        "language": lang,
        "sentiment":result["sentiment"],
        "confidence":result["confidence"],
        "emotion":result["emotion"]
    }
