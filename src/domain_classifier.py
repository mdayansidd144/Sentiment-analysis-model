def detect_domain(text):
    text =text.lower()
    if any(w in text for w in ["movie","film","actor"]):
         return "movie"
    elif any(w in text for w in ["book","author","novel"]):
         return "book"
    elif any(w in text for w in ["government","election","policy"]):
          return "politics"
    elif any(w in text for w in ["game","team","score"]):
          return "sports"
    elif any(w in text for w in ["technology","software","device"]):
          return "technology"
    elif any(w in text for w in ["crime","violence","law"]):
          return "crime"
    else:
         return "general"