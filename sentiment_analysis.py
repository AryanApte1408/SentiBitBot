from transformers import pipeline

def analyze_sentiment_bert(tweets, threshold=0.5):
    sentiment_pipeline = pipeline("sentiment-analysis", device=0)  # Use GPU if available
    
    sentiment_scores = []
    for tweet in tweets:
        result = sentiment_pipeline(tweet)
        score = result[0]['score']
        print(f"Tweet: {tweet}, Sentiment Label: {result[0]['label']}, Score: {score}")  # Print sentiment analysis result
        
        if score >= threshold:
            sentiment_label = result[0]['label']
            compound_score = score if sentiment_label == 'POSITIVE' else -score
            sentiment_scores.append({'compound': compound_score})
        else:
            sentiment_scores.append({'compound': 0})
    
    return sentiment_scores

if __name__ == "__main__":
    sample_tweets = ["Bitcoin is going to the moon!", "I'm worried about the Bitcoin crash.", 
                     "Neutral sentiment about Bitcoin.", "BTC is rising steadily."]
    sentiments = analyze_sentiment_bert(sample_tweets)
    for tweet, sentiment in zip(sample_tweets, sentiments):
        print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
