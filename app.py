# Complete Streamlit app code
# Save this as app.py in the same directory as movies.pkl and similarity.pkl
# Install Streamlit if needed: pip install streamlit
# Run with: streamlit run app.py
# Note: Ensure pandas and other required libraries are installed

import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-family: 'Arial', sans-serif;
        color: #1f2a44;
        text-align: center;
        font-size: 36px;
        margin-bottom: 10px;
    }
    .subtitle {
        font-family: 'Arial', sans-serif;
        color: #4b5e8e;
        text-align: center;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .recommendation-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .recommendation-title {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        font-size: 20px;
        font-weight: bold;
    }
    .recommendation-details {
        font-family: 'Arial', sans-serif;
        color: #34495e;
        font-size: 14px;
    }
    .stButton>button {
        background-color: #4b5e8e;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #1f2a44;
    }
    </style>
""", unsafe_allow_html=True)

# Load the pickled data
@st.cache_data
def load_data():
    movies = pickle.load(open('movies.pkl', 'rb'))
    # Load similarity matrix (chunked or single file)
    try:
        similarity = pickle.load(open('similarity.pkl', 'rb'))
    except FileNotFoundError:
        num_chunks = 10  # Adjust based on your generate_pickles.py
        similarity_chunks = []
        for i in range(num_chunks):
            chunk = pickle.load(open(f'similarity_chunk_{i}.pkl', 'rb'))
            similarity_chunks.append(chunk)
        similarity = np.vstack(similarity_chunks)
    return movies, similarity

# Load data with a loading spinner
with st.spinner("Loading movie data..."):
    movies, similarity = load_data()

# Recommendation function
def recommend(movie, top_n=10):
    movie = movie.lower()
    indices = movies[movies['title'].str.lower() == movie].index
    if len(indices) == 0:
        return [], []
    index = indices[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    recommended_indices = []
    for i in distances[1:top_n+1]:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_indices.append(i[0])
    return recommended_movies, recommended_indices

# Streamlit UI
st.markdown('<div class="title">Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover movies similar to your favorites using content-based filtering on the TMDB 5000 Movie Dataset.</div>', unsafe_allow_html=True)

# Create a container for input controls
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        movie_list = movies['title'].sort_values().values
        selected_movie = st.selectbox("Choose a movie:", movie_list, help="Select a movie to get recommendations.")
    with col2:
        top_n = st.slider("Number of recommendations:", min_value=5, max_value=20, value=10, help="Choose how many recommendations to display.")

# Button to get recommendations
if st.button("Get Recommendations"):
    with st.spinner("Finding recommendations..."):
        recommendations, rec_indices = recommend(selected_movie, top_n=top_n)
        if not recommendations:
            st.error(f"Movie '{selected_movie}' not found in the dataset!")
        else:
            st.markdown(f'<div class="subtitle">Top {top_n} recommendations for "{selected_movie}":</div>', unsafe_allow_html=True)
            # Display recommendations in a styled format
            for i, (rec, idx) in enumerate(zip(recommendations, rec_indices), 1):
                with st.container():
                    st.markdown(f'<div class="recommendation-box">', unsafe_allow_html=True)
                    st.markdown(f'<div class="recommendation-title">{i}. {rec}</div>', unsafe_allow_html=True)
                    # Add movie details (example: tags; you can extend with original dataset if available)
                    tags = movies.iloc[idx]['tags'][:200] + "..." if len(movies.iloc[idx]['tags']) > 200 else movies.iloc[idx]['tags']
                    st.markdown(f'<div class="recommendation-details"><b>Tags:</b> {tags}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<hr><div class="subtitle">Built with Streamlit | Data Source: TMDB 5000 Movie Dataset</div>', unsafe_allow_html=True)

       
