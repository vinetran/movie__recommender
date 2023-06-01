## Building Movie Recommender Project 

### The project aims to build a movie recommender based on movie attributes (title, genre, age certification, production country, actors, imdb score, imdb number of votes, tmdb popularity, tmdb score, duration and description/summary)

### [Project data can be retrieved here] (https://www.kaggle.com/datasets/dgoenrique/netflix-movies-and-tv-shows). The data contains over 19,000 movies titles collected from different movie platforms: Netflix, Amazon prime movies, AppleTV, Disney+, HBO max and Paramount.

### Recommendation is based on the similarity between movies which consists of 2 parts: similarity of the summaries and that of the remaining characteristics. For the first one, an autoencoders model was implemented. Cosine similarity was called for calculating similarites. The final similarity matrix was recuperated by taking average of these 2 similarity scores.

[The application can be reached here] (https://vinetran-movie--recommender-app-tn7gmf.streamlit.app/)

