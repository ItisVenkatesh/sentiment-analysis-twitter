import tweepy
import pandas as pd
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authenticate to Twitter API
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

def collect_tweets(query, max_tweets=100):
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets):
        tweets.append({'tweet': tweet.text, 'created_at': tweet.created_at})
    
    df = pd.DataFrame(tweets)
    df.to_csv('data/raw_data.csv', index=False)

if __name__ == '__main__':
    collect_tweets('sentiment analysis', 100)  # Collect 100 tweets