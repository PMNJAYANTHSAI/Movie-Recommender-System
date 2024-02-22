import streamlit as st 
import pickle
import requests

TMDB_API_KEY = "4ffc200a139cbb86f65e881c9aa818a7"

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id, TMDB_API_KEY)
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:7]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title) 
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# Button to show recommendations
if st.button("Show Recommend"):
    # Use st.spinner to show a loading indicator
    with st.spinner("Finding recommendations..."):
        movie_name, movies_poster = recommend(selectvalue)

    # Display recommendations in columns
        movie_name, movies_poster = recommend(selectvalue)
        col1, col2, col3, col4, col5,col6= st.columns(6)
    with col1:
        st.text(movie_name[0])
        st.image(movies_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movies_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movies_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movies_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movies_poster[4])
    with col6:
        st.text(movie_name[5])
        st.image(movies_poster[5])
