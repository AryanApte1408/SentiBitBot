# logger.py

import logging

logging.basicConfig(filename='trading_bot.log', level=logging.INFO)

def log_trade(decision, sentiment):
    logging.info(f'Trade decision: {decision} - Sentiment: {sentiment}')

if __name__ == "__main__":
    log_trade('buy', 0.5)
