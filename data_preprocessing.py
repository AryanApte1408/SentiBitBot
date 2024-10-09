# data_preprocessing.py

import re
import string

def clean_tweet(tweet):
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove user @ references and '#'
    tweet = re.sub(r'\@\w+|\#','', tweet)
    
    # Remove punctuation and numbers
    tweet = tweet.translate(str.maketrans('', '', string.punctuation + string.digits))
    
    # Convert to lowercase
    tweet = tweet.lower()
    
    return tweet

def preprocess_tweets(tweets):
    return [clean_tweet(tweet) for tweet in tweets]

if __name__ == "__main__":
    sample_tweets = ["Check this out! https://example.com #Bitcoin @user", "I'm loving Bitcoin!!!"]
    clean_tweets = preprocess_tweets(sample_tweets)
    print(clean_tweets)
