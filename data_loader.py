# data_loader.py

import pandas as pd

def load_tweet_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, encoding='ISO-8859-1', header=None)
    
    # Rename the columns for easier access
    df.columns = ['target', 'id', 'date', 'flag', 'user', 'text']
    
    # Extract only the 'text' column for sentiment analysis
    tweets = df['text'].tolist()
    
    return tweets

if __name__ == "__main__":
    tweets = load_tweet_data('sentiment140.csv')
    print(tweets[:5])  # Print the first 5 tweets to verify
