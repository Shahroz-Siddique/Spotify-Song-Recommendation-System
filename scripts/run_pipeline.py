from src.data.make_dataset import load_raw_data, clean_data
from src.features.build_features import normalize_features
from src.models.content_based import get_content_based_recommendations

feature_cols = ['danceability', 'energy', 'loudness', 'valence', 'tempo']
df = load_raw_data('/home/foxtech/SHAHROZ_PROJ/Song Recommendation System/data/dataset.csv.zip')
df = clean_data(df)
df = normalize_features(df, feature_cols)
recs = get_content_based_recommendations(df, 'let me love you (feat. justin bieber)', feature_cols)
print(recs)
