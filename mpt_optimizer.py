import cvxpy as cp
import numpy as np

def get_mpt_weights(df, tickers):
    mu = df.pct_change().mean().values
    S = df.pct_change().cov().values

    n = len(tickers)
    w = cp.Variable(n)
    ret = mu.T @ w 
    risk = cp.quad_form(w, S)  

    objective = cp.Maximize(ret - 0.5 * cp.quad_form(w, S))

    constraints = [cp.sum(w) == 1, w >= 0] 

    problem = cp.Problem(objective, constraints)
    problem.solve()

    optimal_weights = w.value
    return dict(zip(tickers, optimal_weights))

