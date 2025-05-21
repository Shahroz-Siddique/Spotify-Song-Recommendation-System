from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def get_content_based_recommendations(df, song_name, feature_cols, top_n=10):
    song_name = song_name.strip().lower()
    if song_name not in df['track_name'].values:
        raise ValueError("Song not found")

    idx = df[df['track_name'] == song_name].index[0]
    song_features = df.loc[idx, feature_cols].values.reshape(1, -1)
    similarities = cosine_similarity(song_features, df[feature_cols])[0]
    df['similarity'] = similarities
    recommendations = df[df['track_name'] != song_name].sort_values(by='similarity', ascending=False).head(top_n)
    return recommendations[['track_name', 'artists', 'similarity']]


