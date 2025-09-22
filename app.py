# Complete Streamlit app code
# Save this as app.py in the same directory as movies.pkl and similarity.pkl
# Install Streamlit if needed: pip install streamlit
# Run with: streamlit run app.py
# Note: Ensure pandas and other required libraries are installed

import streamlit as st
import pickle
import pandas as pd

# Load the pickled data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function (adapted from the notebook)
def recommend(movie, top_n=10):
    movie = movie.lower()
    indices = movies[movies['title'].str.lower() == movie].index
    if len(indices) == 0:
        return ["Movie not found!"]
    index = indices[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i in distances[1:top_n+1]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title("Movie Recommendation System")
st.write("This app recommends movies similar to a given movie using content-based filtering on the TMDB 5000 Movie Dataset.")

# Dropdown for movie selection
movie_list = movies['title'].sort_values().values
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Slider for top N recommendations
top_n = st.slider("Number of recommendations:", min_value=5, max_value=20, value=10)

# Button to get recommendations
if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie, top_n=top_n)
    if recommendations[0] == "Movie not found!":
        st.error("Movie not found in the dataset!")
    else:
        st.subheader(f"Top {top_n} recommendations for '{selected_movie}':")
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")