import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Get the sentiment scores for the input text
    sentiment_scores = sid.polarity_scores(text)

    # Determine the sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    st.title("Sentiment Analysis with Streamlit")

    st.write("Enter text or list of text (press Enter after each text")

    text_here = st.text_area("Input Text", "").split('\n')

    # Remove any empty strings from the list
    text_here = list(filter(lambda x: x.strip() != '', text_here))

    if st.button("Analyze Sentiment"):
        st.write("Sentiment Analysis Results:")
        for text in text_here:
            sentiment_result = analyze_sentiment(text)
            st.write(f"'{sentiment_result}': {text}")

if __name__ == "__main__":
    main()
