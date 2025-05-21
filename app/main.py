import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data.make_dataset import load_raw_data, clean_data
from src.features.build_features import normalize_features
from src.models.content_based import get_content_based_recommendations

st.title('Spotify Music Recommendation System')
df = load_raw_data('/home/foxtech/SHAHROZ_PROJ/Song Recommendation System/data/dataset.csv.zip')
df = clean_data(df)
feature_cols = ['danceability', 'energy', 'loudness', 'valence', 'tempo']
df = normalize_features(df, feature_cols)

song_list = df['track_name'].drop_duplicates().sort_values().tolist()
song_input = st.selectbox('Search or select a song', song_list)
manual_input = st.text_input('Or enter a song name')

song_to_recommend = manual_input.strip().lower() if manual_input else song_input.strip().lower()


if st.button('Recommend'):
    try:
        recs = get_content_based_recommendations(df, song_to_recommend, feature_cols)
        st.subheader('Recommended Songs')
        st.dataframe(recs)
    except Exception as e:
        st.error(f'Song not found or unable to process. Error: {e}')
