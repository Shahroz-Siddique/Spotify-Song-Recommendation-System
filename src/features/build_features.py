from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalize_features(df, feature_cols):
    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])
    return df
