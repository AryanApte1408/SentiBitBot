
from trading import trading_decision
def backtest_strategy(sentiment_scores, price_data, fee=0.001):
    capital = 1000  # Starting capital in USD
    position = 0  # No position to start with (0 BTC)
    portfolio_log = []  # List to log changes in the portfolio

    for i in range(len(sentiment_scores)):
        decision = trading_decision([sentiment_scores[i]])
        
        if decision == 'buy' and capital > price_data[i]:
            position += 1  # Buy 1 BTC
            capital -= price_data[i] * (1 + fee)  # Account for transaction fee
            portfolio_log.append(f"Buy 1 BTC at {price_data[i]} USD, Capital: {capital:.2f} USD, BTC: {position}")
        elif decision == 'sell' and position > 0:
            position -= 1  # Sell 1 BTC
            capital += price_data[i] * (1 - fee)  # Account for transaction fee
            portfolio_log.append(f"Sell 1 BTC at {price_data[i]} USD, Capital: {capital:.2f} USD, BTC: {position}")

    final_value = capital + position * price_data[-1]  # Final portfolio value
    portfolio_log.append(f"Final Portfolio Value: {final_value:.2f} USD")
    
    # Print the portfolio log to show the changes
    for log in portfolio_log:
        print(log)

    return final_value

if __name__ == "__main__":
    sentiment_scores = [{'compound': 0.2}, {'compound': -0.1}, {'compound': 0.3}, {'compound': -0.2}]
    price_data = [100, 105, 102, 110]
    backtest_strategy(sentiment_scores, price_data)
