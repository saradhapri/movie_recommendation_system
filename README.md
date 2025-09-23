# Movie Recommendation System

This project is a **content-based movie recommendation system** built using **Streamlit** and the **TMDB 5000 Movie Dataset**.  
It allows users to discover movies similar to their favorites by analyzing movie metadata and applying cosine similarity on combined features such as genre, cast, crew, keywords, and overview.

---

## Features
- Content-based filtering using cosine similarity.
- Interactive web interface built with Streamlit.
- Adjustable number of recommendations.
- Recommendations displayed with movie title and tags.

---

## Dataset

The project uses the **TMDB 5000 Movie Dataset** available from Kaggle.  
Since the files are too large to upload, you can download them from the links below:

- [tmdb_5000_movies.csv](https://drive.google.com/file/d/1a16MlcdV2W-HHBYnC1JXkH3gxfVgiaxU/view?usp=sharing)  
- [tmdb_5000_credits.csv](https://drive.google.com/file/d/1rc5uTGqA7D1CSiyfP0fUTruZC2xQ_rK4/view?usp=sharing)

---

## Folder Structure

```

├── data/                      # Data files 
├── demo/                      # Demo images/screenshots
│   ├── img1.png               # Screenshot of input interface
│   ├── img2.png               # Screenshot of recommendation results
├── app.py                     # Main Streamlit app file
├── Movie Recommendation System.ipynb  # Jupyter Notebook for preprocessing & modeling
├── movies.pkl                 # Preprocessed similarity matrix
├── README.md                  # Project documentation

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

3. Ensure the dataset files (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`) are downloaded and placed in the correct path.

4. Run the Streamlit app:

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
* Deploy the app on cloud platforms (Heroku, Streamlit Community Cloud, or AWS).
* Extend recommendation options (e.g., based on actors, directors, or genres specifically).

---

## Built With

* Python
* Streamlit
* Pandas, NumPy
* Scikit-learn
* TMDB 5000 Movie Dataset

---

## Acknowledgements

* Dataset sourced from TMDB 5000 Movie Dataset (Kaggle).
* Inspired by content-based filtering techniques in recommender systems.

---

## License

This project is licensed under the terms of the **MIT License**.


