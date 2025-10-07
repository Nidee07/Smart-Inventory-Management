import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import numpy as np
import pandas as pd

def prepare_data(data, n_steps):
    X, y = [], []
    for i in range(len(data) - n_steps):
        X.append(data[i:i+n_steps])
        y.append(data[i+n_steps])
    return np.array(X), np.array(y)

def create_model(input_shape):
    model = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(sales_data):
    n_steps = 10
    data = sales_data.values
    X, y = prepare_data(data, n_steps)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = create_model((n_steps, 1))
    model.fit(X, y, epochs=50, verbose=1)

    return model

# Example use:
# sales = pd.read_csv('historical_sales.csv')['sales']
# model = train_model(sales)
