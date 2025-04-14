import yfinance as yf
import pandas as pd

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
    return data

def add_technical_indicators(df):
    df['RSI'] = 100 - (100 / (1 + df.pct_change().fillna(0).rolling(window=14).mean() / df.pct_change().fillna(0).rolling(window=14).std()))

    df['MACD'] = df.ewm(span=12, adjust=False).mean() - df.ewm(span=26, adjust=False).mean()
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df
