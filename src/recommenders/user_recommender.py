from src.models.content_based import get_content_based_recommendations
import pandas as pd

def recommend_for_user(df, user_history, feature_cols):
    recommendations = pd.DataFrame()
    for song in user_history:
        try:
            recs = get_content_based_recommendations(df, song, feature_cols)
            recommendations = pd.concat([recommendations, recs])
        except:
            continue
    return recommendations.drop_duplicates().head(10)