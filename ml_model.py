from sklearn.ensemble import RandomForestRegressor
import numpy as np

def train_and_predict_returns(df, tickers):
    features = df[tickers].pct_change().fillna(0).shift(1).dropna()
    target = df[tickers].pct_change().fillna(0).shift(-1).dropna()

    model = RandomForestRegressor(n_estimators=100)
    model.fit(features, target)

    predicted_returns = model.predict(features.tail(1))
    return predicted_returns
