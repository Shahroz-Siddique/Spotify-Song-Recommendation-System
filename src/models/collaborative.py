from sklearn.neighbors import NearestNeighbors
import pandas as pd

def get_collaborative_recommendations(df, user_item_matrix, song_name, top_n=10):
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(user_item_matrix.values)
    song_idx = df[df['track_name'] == song_name].index[0]
    distances, indices = model_knn.kneighbors([user_item_matrix.iloc[song_idx]], n_neighbors=top_n+1)
    return df.iloc[indices[0][1:]][['track_name', 'artists']]
