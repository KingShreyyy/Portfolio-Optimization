import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from data_processing import get_stock_data
from mpt_optimizer import get_mpt_weights  # Import the MPT optimization function

# Define stock tickers
tickers = ['AAPL', 'GOOG', 'AMZN','MSFT', 'TSLA', 'NFLX', 'META', 'NVDA']

# Download stock data using yfinance
def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    
    # Check if 'Adj Close' exists, use 'Close' if not
    if 'Adj Close' in data.columns:
        return data['Adj Close']
    else:
        print("Warning: 'Adj Close' not found, using 'Close' instead.")
        return data['Close']

# Get stock data for a specific date range
stock_data = get_stock_data(tickers, '2019-01-01', '2024-12-31')

# Display first few rows of data to check
print(stock_data.head())

# Perform portfolio optimization using MPT
optimized_portfolio = get_mpt_weights(stock_data, tickers)

# Display optimized portfolio weights
print("Optimized Portfolio Weights (MPT):")
for ticker, weight in optimized_portfolio.items():
    print(f"{ticker}: {weight:.4f}")

# You can visualize the results here, like showing the performance
# For example, plotting the portfolio return
portfolio_return = (stock_data.pct_change() * list(optimized_portfolio.values())).sum(axis=1).cumsum()
plt.plot(portfolio_return)
plt.title("Optimized Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.show()
