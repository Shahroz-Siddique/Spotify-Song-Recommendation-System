import pandas as pd

def get_hybrid_recommendations(content_recs, collab_recs):
    combined = pd.concat([content_recs, collab_recs]).drop_duplicates()
    return combined.head(10)