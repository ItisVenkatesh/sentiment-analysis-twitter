import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\S+', '', text)     # Remove mentions
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters
    return text.lower()

def preprocess_data(input_file='data/raw_data.csv', output_file='data/processed_data.csv'):
    df = pd.read_csv(input_file)
    df['cleaned_tweet'] = df['tweet'].apply(clean_text)
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    preprocess_data()