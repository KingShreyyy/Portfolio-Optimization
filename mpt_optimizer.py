import cvxpy as cp
import numpy as np

# Get MPT weights using cvxpy for optimization
def get_mpt_weights(df, tickers):
    # Calculate expected returns and covariance matrix
    mu = df.pct_change().mean().values
    S = df.pct_change().cov().values

    # Portfolio weights (optimization)
    n = len(tickers)
    w = cp.Variable(n)  # Portfolio weights as a variable
    ret = mu.T @ w  # Expected return
    risk = cp.quad_form(w, S)  # Portfolio risk (variance)

    # Maximize Sharpe Ratio or adjust risk-return tradeoff
    objective = cp.Maximize(ret - 0.5 * cp.quad_form(w, S))  # Adjust the 0.5 to experiment with risk

    constraints = [cp.sum(w) == 1, w >= 0]  # Constraints: weights sum to 1, non-negative

    problem = cp.Problem(objective, constraints)
    problem.solve()

    # Get the optimal portfolio weights
    optimal_weights = w.value
    return dict(zip(tickers, optimal_weights))

