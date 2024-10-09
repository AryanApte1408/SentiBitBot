
# Sentiment-Based Bitcoin Trading Bot

## Overview

This project builds a sentiment-based trading bot using sentiment analysis on tweets to guide buy/sell decisions for Bitcoin. The bot simulates 14 days of trading, where it evaluates daily tweets and uses sentiment analysis and technical indicators (MACD) to make informed trading decisions.

The goal of the bot is to achieve at least a 10% ROI (Return on Investment) by making trades based on the combined sentiment of tweets and MACD signals.

## Features

- Sentiment analysis using **FinBERT** model from HuggingFace.
- Technical indicator integration (MACD - Moving Average Convergence Divergence).
- Daily trading decisions (buy/sell/hold) based on sentiment and MACD signals.
- Simulates portfolio value over 14 days of trading.
- **GPU-Accelerated** sentiment analysis for faster processing.

## Dataset

We use the **Sentiment140** dataset to extract tweets for sentiment analysis. The dataset contains over 1.6 million tweets classified as positive or negative.

You can download the dataset from [Kaggle Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AryanApte1408/sentiment-based-trading-bot.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset from Kaggle and place it in the project directory.

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

- The bot reads daily tweets, performs sentiment analysis using the FinBERT model, and calculates MACD for decision-making.
- Based on the combined sentiment score and MACD signal, the bot decides whether to buy, sell, or hold Bitcoin.

## Requirements

- Python 3.8+
- GPU Support for better performance (Optional but recommended)
- Required libraries can be installed using the `requirements.txt`.

## Results

The bot simulates a 14-day trading session and plots the portfolio value over time. The final portfolio value and ROI are printed at the end of the simulation.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
