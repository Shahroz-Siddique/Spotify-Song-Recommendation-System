from src.data.make_dataset import load_raw_data, clean_data, save_processed_data
from src.features.build_features import normalize_features

if __name__ == '__main__':
    df = load_raw_data('/home/foxtech/SHAHROZ_PROJ/Song Recommendation System/data/dataset.csv.zip')
    df = clean_data(df)
    df = normalize_features(df, ['danceability', 'energy', 'loudness', 'valence', 'tempo'])
    save_processed_data(df, 'data/processed/clean_dataset.csv')