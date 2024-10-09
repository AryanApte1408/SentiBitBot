# data_collection.py

import tweepy
from config import BEARER_TOKEN

def authenticate_twitter_v2():
    # Create a client using the bearer token for v2 API
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    return client

def fetch_tweets_v2(keyword, count=10):
    client = authenticate_twitter_v2()
    # Use the search_recent_tweets method available in API v2
    response = client.search_recent_tweets(query=keyword, max_results=count, tweet_fields=['created_at', 'lang'])
    # Extract tweet texts from the response
    tweet_texts = [tweet.text for tweet in response.data] if response.data else []
    return tweet_texts

if __name__ == "__main__":
    tweets = fetch_tweets_v2("bitcoin", 10)
    for tweet in tweets:
        print(tweet)
