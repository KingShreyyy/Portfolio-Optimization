import yfinance as yf
import pandas as pd

# Download stock data
def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
    return data

# Add technical indicators (RSI, MACD)
def add_technical_indicators(df):
    # RSI
    df['RSI'] = 100 - (100 / (1 + df.pct_change().fillna(0).rolling(window=14).mean() / df.pct_change().fillna(0).rolling(window=14).std()))
    # MACD
    df['MACD'] = df.ewm(span=12, adjust=False).mean() - df.ewm(span=26, adjust=False).mean()
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df
