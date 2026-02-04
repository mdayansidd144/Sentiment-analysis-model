import sys
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_sentiment
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
    .title {text-align: center; font-size: 40px; font-weight: bold;}
    .subtitle {text-align: center; color: gray;}
    .box {padding: 15px; border-radius: 10px; background-color: #1f2937;}
</style>
""", unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []
st.markdown("<div class='title'>🤖 Sentiment Intelligence System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Multi-Domain | Emotion Aware | AI Powered</div>", unsafe_allow_html=True)
st.write("")
text = st.text_area("Enter your text:", height=220)
col1, col2 = st.columns(2)
with col1:
    analyze = st.button("Analyze")
with col2:
    clear = st.button("🗑 Clear History")
if clear:
    st.session_state.history.clear()
    st.success("History cleared!")
if analyze and text.strip() != "":
    result = predict_sentiment(text)
    st.session_state.history.append(result)
    st.markdown("### 📊 Analysis Result")
    st.success(f"**Sentiment:** {result['sentiment']}")
    st.markdown(" Confidence Level")
    st.progress(int(result["confidence"] * 100))
    st.write(f"Confidence: **{round(result['confidence']*100, 2)}%**")
    st.markdown("##Emotion Strength")
    emotions = {
        "Positive": result["confidence"],
        "Neutral": 1 - abs(result["confidence"] - 0.5),
        "Negative": 1 - result["confidence"]
    }

    fig, ax = plt.subplots()
    ax.bar(emotions.keys(), emotions.values(), color=["green", "orange", "red"])
    ax.set_ylabel("Intensity")
    ax.set_title("Emotion Distribution")
    st.pyplot(fig)
if len(st.session_state.history) > 1:
    st.markdown("## Sentiment Trend")
    scores = [h["confidence"] for h in st.session_state.history]

    fig, ax = plt.subplots()
    ax.plot(scores, marker="o")
    ax.set_title("Sentiment Over Time")
    ax.set_ylabel("Confidence")
    ax.set_xlabel("Input Count")
    st.pyplot(fig)
st.markdown("---")
st.caption("AI Sentiment System | Built for Tech Expo")
# import streamlit as st
# from src.movie_sentiment_controller import analyze_imdb_movie
# from src.ecg_visualizer import plot_ecg

# st.set_page_config(layout="wide", page_title="IMDb Sentiment AI")

# st.markdown("<h1 style='text-align:center;'>🎬 IMDb Sentiment Intelligence</h1>", unsafe_allow_html=True)

# movie = st.text_input("Enter Movie Name")

# if st.button("Analyze Movie"):
#     result = analyze_imdb_movie(movie)

#     if "error" in result:
#         st.error("Movie not found")
#     else:
#         meta = result["meta"]

#         st.subheader(meta["title"])
#         st.caption(f"{meta['year']} | {meta['genre']}")

#         col1, col2 = st.columns(2)

#         with col1:
#             st.markdown("### 🧠 Plot Sentiment")
#             st.success(result["plot_sentiment"]["sentiment"].upper())
#             st.progress(int(result["plot_sentiment"]["confidence"] * 100))

#         with col2:
#             st.markdown("### ⭐ IMDb Rating")
#             st.metric("Rating", meta["rating"])

#         st.markdown("### 📊 Public Review Sentiment")
#         st.bar_chart(result["review_summary"])

#         st.markdown("### 💓 Audience Sentiment Waveform")
#         fig = plot_ecg(result["timeline"])
#         st.pyplot(fig)

# )
# st.markdown("""
# <style>
# body {
#     background-color: #0f172a;
#     color: #e5e7eb;import sys
# import os
# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from src.movie_analyzer import analyze_movie_by_name
# from src.predict import predict_sentiment
# st.set_page_config(
#     page_title="Sentiment Intelligence AI",
#     page_icon="🧠",
#     layout="wide"
# }
# .card {
#     background: rgba(255,255,255,0.05);
#     border-radius: 15px;
#     padding: 20px;
#     margin-bottom: 20px;
#     box-shadow: 0 0 20px rgba(0,255,255,0.08);
# }
# .title {
#     font-size: 42px;
#     font-weight: bold;
#     text-align: center;
# }
# .subtitle {
#     text-align: center;
#     color: #94a3b8;
# }
# .metric {
#     font-size: 28px;
#     font-weight: bold;
# }
# </style>
# """, unsafe_allow_html=True)
# st.markdown("<div class='title'>🧠 Sentiment Intelligence AI</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle'>Movies • Geopolitics • Tech • Sports • Public Opinion</div>", unsafe_allow_html=True)
# st.write("")
# tab1, tab2 = st.tabs(["🎬 Movie Analyzer", "💬 Text Sentiment Analyzer"])
# with tab1:
#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     movie = st.text_input("🎞 Enter Movie Name (IMDb):", placeholder="Inception")
#     if st.button("🚀 Analyze Movie"):
#         result = analyze_movie_by_name(movie)
#         if "error" in result:
#             st.error("❌ Movie not found")
#         else:
#             col1, col2, col3 = st.columns(3)

#             with col1:
#                 st.metric("⭐ IMDb Rating", result["rating"])
#             with col2:
#                 st.metric("🧠 Plot Sentiment", result["plot_sentiment"])
#             with col3:
#                 st.metric("📊 Verdict", result["verdict"])
#             st.markdown("### 🔍 AI Confidence")
#             st.progress(int(result["confidence"] * 100))
#             st.write(f"Confidence: **{round(result['confidence']*100,2)}%**")

#     st.markdown("</div>", unsafe_allow_html=True)
# with tab2:
#     st.markdown("<div class='card'>", unsafe_allow_html=True)
#     text = st.text_area("✍ Enter any text:", height=190)

#     if st.button("🔍 Analyze Text"):
#         result = predict_sentiment(text)

#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric("🧠 Sentiment", result["sentiment"])
#             st.metric("🌐 Domain", result["domain"])

#         with col2:
#             st.markdown("### 🔎 Confidence")
#             st.progress(int(result["confidence"] * 100))
#             st.write(f"{round(result['confidence']*100,2)}%")
#         st.markdown("### 😊 Emotion Intensity")
#         emotions = {
#             "Positive": result["confidence"],
#             "Neutral": 1 - abs(result["confidence"] - 0.5),
#             "Negative": 1 - result["confidence"]
#         }
#         fig, ax = plt.subplots()
#         ax.bar(emotions.keys(), emotions.values(), color=["#22c55e", "#eab308", "#ef4444"])
#         ax.set_ylabel("Intensity")
#         ax.set_facecolor("#0f172a")
#         fig.patch.set_facecolor("#0f172a")
#         st.pyplot(fig)

#     st.markdown("</div>", unsafe_allow_html=True)
# st.markdown("---")
# st.caption("🚀 Built with AI | Optimized for Tech Expo | Real-World Sentiment Intelligence")
