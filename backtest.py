import numpy as np
import matplotlib.pyplot as plt

def backtest_portfolio(df, tickers, mpt_weights, rl_weights):
    mpt_returns = df[tickers].pct_change().fillna(0).dot(list(mpt_weights.values()))
    rl_returns = df[tickers].pct_change().fillna(0).dot(rl_weights)

    mpt_cumulative = (1 + mpt_returns).cumprod() - 1
    rl_cumulative = (1 + rl_returns).cumprod() - 1

    plt.plot(mpt_cumulative, label='MPT Portfolio')
    plt.plot(rl_cumulative, label='RL Portfolio')
    plt.legend()
    plt.title("Portfolio Performance Comparison")
    plt.show()
