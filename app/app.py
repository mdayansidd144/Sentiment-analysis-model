import sys
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_sentiment
from src.movie_sentiment_controller import analyze_imdb_movie
from src.ecg_visualizer import plot_ecg
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
.title {text-align: center; font-size: 40px; font-weight: bold;}
.subtitle {text-align: center; color: #9ca3af;}
.card {
    padding: 18px;
    border-radius: 12px;
    background-color: #0f172a;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []
st.markdown("<div class='title'>🤖 Sentiment Intelligence System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Text • IMDb Movies • Public Opinion</div>", unsafe_allow_html=True)
st.write("")
tab1, tab2 = st.tabs(["💬 General Text Analysis", "🎬 IMDb Movie Analysis"])
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    text = st.text_area("Enter your text:", height=220)

    col1, col2 = st.columns(2)
    with col1:
        analyze_text = st.button("Analyze Text")
    with col2:
        clear = st.button("🗑 Clear History")

    if clear:
        st.session_state.history.clear()
        st.success("History cleared!")

    if analyze_text and text.strip():
        result = predict_sentiment(text)
        st.session_state.history.append(result)
        st.markdown("### 📊 Analysis Result")
        st.success(f"**Sentiment:** {result['sentiment'].upper()}")

        st.markdown("### Confidence Level")
        st.progress(int(result["confidence"] * 100))
        st.write(f"Confidence: **{round(result['confidence'] * 100, 2)}%**")
        st.markdown("### Emotion Strength")
        emotions = {
            "Positive": result["confidence"],
            "Neutral": 1 - abs(result["confidence"] - 0.5),
            "Negative": 1 - result["confidence"]
        }

        fig, ax = plt.subplots()
        ax.bar(emotions.keys(), emotions.values(), color=["#22c55e", "#facc15", "#ef4444"])
        ax.set_ylabel("Intensity")
        ax.set_title("Emotion Distribution")
        st.pyplot(fig)

    if len(st.session_state.history) > 1:
        st.markdown("### 📈 Sentiment Trend")
        scores = [h["confidence"] for h in st.session_state.history]

        fig, ax = plt.subplots()
        ax.plot(scores, marker="o", color="#38bdf8")
        ax.set_ylabel("Confidence")
        ax.set_xlabel("Input Count")
        st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    movie = st.text_input("🎬 Enter IMDb Movie Name (e.g., Inception)")

    analyze_movie = st.button("Analyze Movie")

    if analyze_movie and movie.strip():
        with st.spinner("Analyzing IMDb data..."):
            result = analyze_imdb_movie(movie)

        if "error" in result:
            st.error("Movie not found. Please try another title.")
        else:
            meta = result["meta"]

            st.subheader(meta["title"])
            st.caption(f"{meta['year']} | {meta['genre']}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🧠 Plot Sentiment")
                st.success(result["plot_sentiment"]["sentiment"].upper())
                st.progress(int(result["plot_sentiment"]["confidence"] * 100))

            with col2:
                st.markdown("### ⭐ IMDb Rating")
                st.metric("Rating", meta["rating"])
                st.write(f"Votes: {meta['votes']}")

            if result["review_summary"]:
                st.markdown("### 📊 Public Review Sentiment")
                st.bar_chart(result["review_summary"])

            else:
                st.warning("IMDb review dataset not available. Showing plot sentiment only.")

            if result["timeline"]:
                st.markdown("### 💓 Audience Sentiment Waveform")
                fig = plot_ecg(result["timeline"])
                if fig:
                    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.caption("🚀 AI Sentiment Intelligence System | Tech Expo Ready")
