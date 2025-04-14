import numpy as np
import tensorflow as tf

# Define a simple Neural Network for RL
def train_rl_agent(df, tickers):
    # Placeholder for simplified RL agent logic
    returns = df.pct_change().dropna()
    state_dim = len(tickers)
    action_dim = len(tickers)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(state_dim,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(action_dim, activation='softmax')
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    # Placeholder: Train model and return predicted portfolio weights
    latest_state = returns.values[-1].reshape(1, -1)
    rl_weights = model.predict(latest_state)[0]
    rl_weights /= np.sum(rl_weights)  # Normalize to sum = 1
    return rl_weights
