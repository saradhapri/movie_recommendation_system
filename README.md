# Movie Recommendation System

This project is a **content-based movie recommendation system** built using **Streamlit** and the **TMDB 5000 Movie Dataset**.  
It allows users to discover movies similar to their favorites by analyzing movie metadata and applying cosine similarity on combined features such as genre, cast, crew, keywords, and overview.

---

## Live Demo

👉 [Click here to try the app](https://movie-recommender-system7.streamlit.app/)

---

## Features
- Content-based filtering using cosine similarity.
- Interactive web interface built with Streamlit.
- Adjustable number of recommendations.
- Recommendations displayed with movie title and tags.

---

## Dataset

The project uses the **TMDB 5000 Movie Dataset**, which is already included in this repository under the `data/` folder:

- [tmdb_5000_movies.csv](data/tmdb_5000_movies.csv)  
- [tmdb_5000_credits.csv](data/tmdb_5000_credits.csv)  

Preprocessed files (`movies.pkl` and `similarity.pkl`) are stored in the project root for faster loading during app execution.

---

## Folder Structure

```

├── data/
│   ├── tmdb\_5000\_movies.csv     # Movies dataset
│   ├── tmdb\_5000\_credits.csv    # Credits dataset
├── demo/
│   ├── img1.png                 # Screenshot of input interface
│   ├── img2.png                 # Screenshot of recommendation results
├── app.py                       # Main Streamlit app file
├── Movie Recommendation System.ipynb   # Jupyter Notebook for preprocessing & modeling
├── movies.pkl                   # Preprocessed movie data (root)
├── similarity.pkl               # Precomputed similarity matrix (root)
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation

````

---

## Screenshots

### Input Interface
![Input Interface](demo/img1.png)

### Recommendation Output
![Recommendation Output](demo/img2.png)

---

## Project Workflow

1. **Data Collection** → Import TMDB 5000 dataset (`movies.csv`, `credits.csv`).  
2. **Preprocessing** → Clean missing values, extract features (genres, keywords, cast, crew, overview), and build tags.  
3. **EDA** → Explore relationships between features, analyze distribution of genres/keywords, inspect dataset consistency.  
4. **Modeling** → Use `CountVectorizer` and cosine similarity to compute similarity between movies.  
5. **Evaluation** → Test recommendations manually for accuracy and relevance.  
6. **Deployment** → Deploy interactive web app using **Streamlit**.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/saradhapri/movie_recommendation_system.git
   cd movie_recommendation_system
   ````

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the dataset files are available in the `data/` folder:

   * `data/tmdb_5000_movies.csv`
   * `data/tmdb_5000_credits.csv`

4. Ensure the preprocessed pickle files are available in the project root:

   * `movies.pkl`
   * `similarity.pkl`

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## Results & Conclusion

* The content-based model provides **reliable and relevant recommendations** based on movie similarity.
* Users can adjust the number of recommendations dynamically.
* Insights: Combining multiple metadata fields (cast, crew, genres, keywords, overview) improves recommendation quality compared to using a single feature.
* The system works well for popular movies and provides meaningful suggestions.

---

## Future Improvements

* Add **hybrid filtering** (combine content-based + collaborative filtering).
* Integrate **poster images and metadata** from TMDB API for richer UI.
* Optimize similarity calculations for faster performance on larger datasets.
* Extend recommendation options (e.g., based on actors, directors, or genres specifically).

---

## Built With

* Python
* Streamlit
* Pandas, NumPy
* Scikit-learn
* TMDB 5000 Movie Dataset
* TMDB 5000 Credit Dataset

---

## Acknowledgements

* Dataset sourced from TMDB 5000 Movie Dataset (Kaggle).
* Inspired by content-based filtering techniques in recommender systems.

---

## License

This project is licensed under the terms of the **MIT License**.
