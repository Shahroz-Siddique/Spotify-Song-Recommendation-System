from src.models.content_based import get_content_based_recommendations

def recommend_similar_items(df, song_name, feature_cols):
    return get_content_based_recommendations(df, song_name, feature_cols)