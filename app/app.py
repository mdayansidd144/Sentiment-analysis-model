import streamlit as st
from src.predict import predict_sentiment
st.title("Welcome to Sentiment Analysis mode")
text = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    result = predict_sentiment(text)
    st.write("Domain:",result["domain"])
    st.write("Sentiment:",result["Sentiment"])
    st.write("Confidence:",result["confidence"])