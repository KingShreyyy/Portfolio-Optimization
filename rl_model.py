import numpy as np
import tensorflow as tf

def train_rl_agent(df, tickers):

    returns = df.pct_change().dropna()
    state_dim = len(tickers)
    action_dim = len(tickers)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(state_dim,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(action_dim, activation='softmax')
    ])

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    latest_state = returns.values[-1].reshape(1, -1)
    rl_weights = model.predict(latest_state)[0]
    rl_weights /= np.sum(rl_weights) 
    return rl_weights
