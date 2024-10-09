# technical_analysis.py

import pandas as pd
import pandas_ta as ta  # Using pandas-ta for technical analysis

def calculate_technical_indicators(df):
    # Calculate Simple Moving Average (SMA)
    df['SMA_14'] = ta.sma(df['close'], length=14)
    
    # Calculate Relative Strength Index (RSI)
    df['RSI_14'] = ta.rsi(df['close'], length=14)
    
    return df

if __name__ == "__main__":
    # Example DataFrame with closing prices
    data = {'close': [120, 121, 119, 117, 118, 120, 122, 121, 120, 119, 118, 117, 116, 115, 116]}
    df = pd.DataFrame(data)
    
    df = calculate_technical_indicators(df)
    print(df)
