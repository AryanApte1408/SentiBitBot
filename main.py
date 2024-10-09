#approach 1 using base dilbert not finbert

# import logging
# import random
# import pandas as pd
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# from sentiment_analysis import analyze_sentiment_bert
# from trading import trading_decision, calculate_macd

# # Initialize logging
# logging.basicConfig(level=logging.INFO)

# sentiment140 = pd.read_csv("sentiment140.csv", encoding="ISO-8859-1", header=None)
# sentiment140.columns = ["target", "ids", "date", "flag", "user", "text"]

# # Get only the "text" column for tweets
# all_tweets = sentiment140['text'].tolist()

# # Randomly simulate 14 days with a varying number of tweets per day (e.g., 5 to 10 tweets per day)
# tweets_per_day = [random.sample(all_tweets, random.randint(5, 10)) for _ in range(14)]

# # Starting portfolio value
# portfolio_value = 1000
# portfolio_history = [portfolio_value]

# # Placeholder for price data to calculate MACD (use dummy prices or actual data if available)
# price_data = [random.uniform(100, 200) for _ in range(14)]  # Example price data

# # Simulate the 14 days of trading
# for day, (tweets, price) in enumerate(zip(tweets_per_day, price_data), start=1):
#     logging.info(f"Processing day {day}")
    
#     # Analyze sentiment for the day's tweets
#     sentiment_scores = analyze_sentiment_bert(tweets)
    
#     # Calculate MACD signal for the day using price data
#     macd_signal = calculate_macd(price_data[:day+1])  # Calculate MACD based on available price data
    
#     # Compute average sentiment score
#     avg_sentiment = sum([score['compound'] for score in sentiment_scores]) / len(sentiment_scores)
    
#     # Adjust thresholds for sentiment and MACD
#     if avg_sentiment > 0.8 and macd_signal == 'buy':
#         decision = 'buy'
#     elif avg_sentiment < -0.8 and macd_signal == 'sell':
#         decision = 'sell'
#     else:
#         decision = 'hold'
    
#     logging.info(f"Day {day}: Trade decision: {decision} - Average Sentiment: {avg_sentiment}, MACD Signal: {macd_signal}")

#     # Simulate portfolio changes based on decisions (more aggressive changes)
#     if decision == 'buy':
#         portfolio_value += portfolio_value * 0.015  # Buy increases by 1.5%
#     elif decision == 'sell':
#         portfolio_value -= portfolio_value * 0.015  # Sell decreases by 1.5%
    
#     portfolio_history.append(portfolio_value)

# # Plot the portfolio value change over time
# plt.figure(figsize=(10, 6))
# plt.plot(range(1, len(portfolio_history) + 1), portfolio_history, marker='o')
# plt.title("Portfolio Value Over 14 Days")
# plt.xlabel("Day")
# plt.ylabel("Portfolio Value ($)")
# plt.grid(True)
# plt.savefig('portfolio_value.png')  # Save the figure instead of displaying it

# # Print final portfolio value
# logging.info(f"Final Portfolio Value: ${portfolio_value:.2f}")
# logging.info(f"ROI: {((portfolio_value / portfolio_history[0]) - 1) * 100:.2f}%")


#approach 2 using finbert

import logging
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from transformers import pipeline
from trading import trading_decision, calculate_macd
import torch

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Load FinBERT sentiment analysis pipeline and set device to GPU (device=0)
device = 0 if torch.cuda.is_available() else -1  # Use GPU if available, otherwise CPU
sentiment_pipeline = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone", return_all_scores=True, device=device)

# Load Sentiment140 dataset
sentiment140 = pd.read_csv("sentiment140.csv", encoding="ISO-8859-1", header=None)
sentiment140.columns = ["target", "ids", "date", "flag", "user", "text"]

# Get all the tweets
all_tweets = sentiment140['text'].tolist()

# Instead of sampling a random subset, use all tweets for each day.
# Split the data into chunks, simulating 14 days (for example, assume the data is already sorted chronologically)
tweets_per_day = [all_tweets[i::14] for i in range(14)]  # Split into 14 days

# Starting portfolio value
portfolio_value = 1000
portfolio_history = [portfolio_value]

# Placeholder for price data to calculate MACD (use dummy prices or actual data if available)
price_data = [150 + i * 0.5 for i in range(14)]  # Example price data increasing slightly each day

# Function to analyze sentiment using FinBERT
def analyze_sentiment_finbert(tweets):
    sentiment_scores = []
    for tweet in tweets:
        logging.info(f"Tweet: {tweet}")
        result = sentiment_pipeline(tweet)
        positive_score = result[0][0]['score'] if result[0][0]['label'] == 'POSITIVE' else -result[0][0]['score']
        negative_score = result[0][1]['score'] if result[0][1]['label'] == 'NEGATIVE' else -result[0][1]['score']
        # You can also include NEUTRAL scores if needed
        sentiment_scores.append(positive_score - negative_score)
    return sentiment_scores

# Simulate the 14 days of trading
for day, (tweets, price) in enumerate(zip(tweets_per_day, price_data), start=1):
    logging.info(f"Processing day {day}")
    
    # Analyze sentiment for the day's tweets using FinBERT
    sentiment_scores = analyze_sentiment_finbert(tweets)
    
    # Calculate MACD signal for the day using price data
    macd_signal = calculate_macd(price_data[:day+1])  # Calculate MACD based on available price data
    
    # Compute average sentiment score
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    
    # Complex thresholding: combine sentiment and MACD signals
    if avg_sentiment > 0.4 and macd_signal == 'buy':  # Adjust threshold for more trades
        decision = 'buy'
    elif avg_sentiment < -0.4 and macd_signal == 'sell':  # Adjust threshold for more trades
        decision = 'sell'
    else:
        decision = 'hold'
    
    logging.info(f"Day {day}: Trade decision: {decision} - Average Sentiment: {avg_sentiment}, MACD Signal: {macd_signal}")

    # Simulate portfolio changes based on decisions
    if decision == 'buy':
        portfolio_value += portfolio_value * 0.03  # Buy increases by 3%
    elif decision == 'sell':
        portfolio_value -= portfolio_value * 0.03  # Sell decreases by 3%
    
    portfolio_history.append(portfolio_value)

# Plot the portfolio value change over time
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(portfolio_history) + 1), portfolio_history, marker='o')
plt.title("Portfolio Value Over 14 Days")
plt.xlabel("Day")
plt.ylabel("Portfolio Value ($)")
plt.grid(True)
plt.savefig('portfolio_value.png')  # Save the figure instead of displaying it

# Print final portfolio value
logging.info(f"Final Portfolio Value: ${portfolio_value:.2f}")
logging.info(f"ROI: {((portfolio_value / portfolio_history[0]) - 1) * 100:.2f}%")
