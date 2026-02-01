import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from src.predict import predict_sentiment
st.title("Welcome to Sentiment Analysis mode")
text = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    result = predict_sentiment(text)
    st.json(result)