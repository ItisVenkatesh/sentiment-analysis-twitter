from textblob import TextBlob
import pandas as pd

def analyze_sentiment(input_file='data/processed_data.csv', output_file='data/sentiment_results.csv'):
    df = pd.read_csv(input_file)
    
    def get_sentiment(text):
        blob = TextBlob(text)
        return 'positive' if blob.sentiment.polarity > 0 else 'negative'
    
    df['sentiment'] = df['cleaned_tweet'].apply(get_sentiment)
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    analyze_sentiment()