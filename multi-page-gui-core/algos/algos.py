import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

def clean_data(data):
    ...
    return data.dropna().drop_duplicates()

def predict(data):
    model = LinearRegression()
    model.fit(data[["x"]], data[["y"]])
    data["y_pred"] = model.predict(data[["x"]])
    return data

def evaluate(data):
    ...
    return np.random.rand()