import sys
import os
from dotenv import load_dotenv
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv(os.path.join(BASE_DIR, ".env"))
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_sentiment
from src.movie_sentiment_controller import analyze_imdb_movie
from src.ecg_visualizer import plot_ecg
from src.public_opinion_controller import analyze_topic
from src.news_sentiment_controller import analyze_news_topic         
from src.youtube_sentiment_controller import analyze_youtube_video    
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: #e5e7eb;
}
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 1px;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 20px;
}
.card {
    padding: 22px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    margin-bottom: 20px;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 40px rgba(0,0,0,0.55);
}
.stButton>button {
    width: 100%;
    border-radius: 14px;
    padding: 10px 16px;
    font-weight: 600;
    background: linear-gradient(135deg, #22c55e, #38bdf8);
    color: black;
    border: none;
    transition: all 0.25s ease;
}
.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 18px rgba(56,189,248,0.6);
}
textarea, input {
    border-radius: 14px !important;
}
button[data-baseweb="tab"] {
    font-size: 15px;
    padding: 10px;
    transition: color 0.2s ease;
}
button[data-baseweb="tab"]:hover {
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []
st.markdown("<div class='title'>🤖 Sentiment Intelligence System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Text • IMDb • Public Opinion • News • YouTube</div>", unsafe_allow_html=True)
st.write("")
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💬 General Text",
    "🎬 IMDb Movies",
    "🌍 Public Opinion",
    "📰 News Opinion",
    "▶️ YouTube Opinion"
])
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

        st.success(f"**Sentiment:** {result['sentiment'].upper()}")
        st.progress(int(result["confidence"] * 100))
        st.write(f"Confidence: **{round(result['confidence']*100,2)}%**")

        emotions = {
            "Positive": result["confidence"],
            "Neutral": 1 - abs(result["confidence"] - 0.5),
            "Negative": 1 - result["confidence"]
        }

        fig, ax = plt.subplots()
        ax.bar(emotions.keys(), emotions.values(),
               color=["#22c55e", "#facc15", "#ef4444"])
        st.pyplot(fig)

    if len(st.session_state.history) > 1:
        scores = [h["confidence"] for h in st.session_state.history]
        fig, ax = plt.subplots()
        ax.plot(scores, marker="o", color="#38bdf8")
        ax.set_ylabel("Confidence")
        ax.set_xlabel("Input Count")
        st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    movie = st.text_input("Enter IMDb Movie Name (e.g., Inception)")
    if st.button("Analyze Movie"):
        with st.spinner("Analyzing IMDb data..."):
            result = analyze_imdb_movie(movie)

        if "error" in result:
            st.error("Movie not found")
        else:
            meta = result["meta"]
            st.subheader(meta["title"])
            st.caption(f"{meta['year']} | {meta['genre']}")

            col1, col2 = st.columns(2)
            with col1:
                st.success(result["plot_sentiment"]["sentiment"].upper())
                st.progress(int(result["plot_sentiment"]["confidence"] * 100))
            with col2:
                st.metric("IMDb Rating", meta["rating"])
                st.write(f"Votes: {meta['votes']}")

            if result["review_summary"]:
                st.bar_chart(result["review_summary"])

            if result["timeline"]:
                fig = plot_ecg(result["timeline"])
                if fig:
                    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    topic = st.selectbox(
        "Select Topic",
        ["Social Media", "Geopolitics", "Technology", "Sports"]
    )

    if st.button("Analyze Public Opinion"):
        result = analyze_topic(topic)

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader(f"Public Opinion: {topic}")
            st.bar_chart(result["summary"])
            if result["timeline"]:
                st.pyplot(plot_ecg(result["timeline"]))

    st.markdown("</div>", unsafe_allow_html=True)
with tab4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    news_topic = st.text_input("Enter news topic (e.g., geopolitics, AI, elections)")
    if st.button("Analyze News Sentiment"):
        with st.spinner("Fetching live news sentiment..."):
            result = analyze_news_topic(news_topic)

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader(f"News Sentiment: {news_topic}")
            st.bar_chart(result["summary"])
            if result["timeline"]:
                st.pyplot(plot_ecg(result["timeline"]))

    st.markdown("</div>", unsafe_allow_html=True)
with tab5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    video_id = st.text_input("Enter YouTube Video ID")
    if st.button("Analyze YouTube Comments"):
        with st.spinner("Fetching YouTube comments..."):
            result = analyze_youtube_video(video_id)

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("YouTube Comment Sentiment")
            st.bar_chart(result["summary"])
            if result["timeline"]:
                st.pyplot(plot_ecg(result["timeline"]))

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption(
    "🚀 Sentiment Intelligence System | "
    "Live News • YouTube • Datasets • User Input | Tech Expo Ready"
)
