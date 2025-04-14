Portfolio Optimization using Modern Portfolio Theory

This project focuses on portfolio optimization using the principles of Modern Portfolio Theory (MPT). It aims to determine the optimal allocation of assets that maximizes return for a given level of risk.

Overview:
The program fetches historical stock price data, calculates expected returns and the covariance matrix, and applies convex optimization techniques to generate the most efficient portfolio. The optimization process is based on maximizing the Sharpe Ratio.

Features:

Fetches historical stock prices using yfinance

Computes expected returns and covariance of selected assets

Uses cvxpy for solving the optimization problem

Displays historical stock prices and the final optimized portfolio weights

Technologies Used:
Python, Pandas, NumPy, yfinance, cvxpy, Matplotlib

How to Run:

Clone the repository
git clone https://github.com/KingShreyyy/Portfolio-Optimization.git
cd Portfolio-Optimization

Install the required dependencies
pip install -r requirements.txt

Run the main script
python main.py

Customization:
To analyze different stocks, update the tickers list in main.py with your preferred company tickers. You can also modify the date range to change the analysis window.

Example Output:

Displays a plot of historical stock prices

Prints the calculated optimal portfolio weights

License:
This project is open-source and licensed under the MIT License.
