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
text = st.text_area("Enter your text:", height=120)
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
