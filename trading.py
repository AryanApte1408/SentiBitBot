import numpy as np

def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    
    # Helper function to calculate Exponential Moving Average (EMA)
    def ema(prices, window):
        ema_values = []
        multiplier = 2 / (window + 1)
        for i, price in enumerate(prices):
            if i == 0:
                ema_values.append(price)
            else:
                ema_values.append((price - ema_values[i-1]) * multiplier + ema_values[i-1])
        return ema_values

    # Calculate the short-term and long-term EMA
    short_ema = ema(prices, short_window)
    long_ema = ema(prices, long_window)

    # MACD line is the difference between short-term and long-term EMA
    macd = np.array(short_ema) - np.array(long_ema)

    # Signal line is the EMA of the MACD line
    signal_line = ema(macd, signal_window)

    return macd, signal_line

def trading_decision(avg_sentiment, macd_value, signal_value):

    # More complex threshold-based decision-making using both sentiment and MACD
    if avg_sentiment > 0 and macd_value > signal_value:
        return 'buy'
    elif avg_sentiment < 0 and macd_value < signal_value:
        return 'sell'
    else:
        return 'hold'
