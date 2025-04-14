from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Train the model and predict returns
def train_and_predict_returns(df, tickers):
    # Prepare data for ML model (using last 30 days for prediction)
    features = df[tickers].pct_change().fillna(0).shift(1).dropna()
    target = df[tickers].pct_change().fillna(0).shift(-1).dropna()

    # Train a random forest model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(features, target)

    # Predict returns for next period
    predicted_returns = model.predict(features.tail(1))
    return predicted_returns
