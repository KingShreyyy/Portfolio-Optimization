import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from data_processing import get_stock_data
from mpt_optimizer import get_mpt_weights

tickers = ['AAPL', 'GOOG', 'AMZN','MSFT', 'TSLA', 'NFLX', 'META', 'NVDA']

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    
    if 'Adj Close' in data.columns:
        return data['Adj Close']
    else:
        print("Warning: 'Adj Close' not found, using 'Close' instead.")
        return data['Close']

stock_data = get_stock_data(tickers, '2019-01-01', '2024-12-31')

print(stock_data.head())

optimized_portfolio = get_mpt_weights(stock_data, tickers)

print("Optimized Portfolio Weights (MPT):")
for ticker, weight in optimized_portfolio.items():
    print(f"{ticker}: {weight:.4f}")

portfolio_return = (stock_data.pct_change() * list(optimized_portfolio.values())).sum(axis=1).cumsum()
plt.plot(portfolio_return)
plt.title("Optimized Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.show()
