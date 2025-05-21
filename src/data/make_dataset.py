import pandas as pd
import os

def load_raw_data(filepath):
    return pd.read_csv('/home/foxtech/SHAHROZ_PROJ/Song Recommendation System/data/dataset.csv.zip')

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df['track_name'] = df['track_name'].str.strip().str.lower()
    return df

def save_processed_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)