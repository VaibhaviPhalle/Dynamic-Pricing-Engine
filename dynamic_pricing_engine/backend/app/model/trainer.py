# Simple example trainer using scikit-learn to fit a regression for price multiplier.
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_and_save(sample_csv: str, out_model_path: str = 'price_model.joblib'):
    df = pd.read_csv(sample_csv)
    # expected columns: base_price,demand,supply,time_of_day,competitor_price,target_price
    df = df.fillna(method='ffill').fillna(0)
    X = df[['base_price','demand','supply','time_of_day','competitor_price']].values
    y = df['target_price'].values
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, out_model_path)
    print(f"Saved model to {out_model_path}")

if __name__ == '__main__':
    sample = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'sample_data.csv')
    train_and_save(sample, out_model_path='price_model.joblib')
