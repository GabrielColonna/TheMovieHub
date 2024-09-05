import streamlit as st
import requests
import pandas as pd
import numpy as np
import pydeck as pdk
import random


# Gabriel Colonna

st.set_page_config(
    page_title= "The Movie Hub",
    page_icon= "🍿",
    layout="wide",
    initial_sidebar_state="expanded",
)

api_key = 'da4d3949727c3d7c404e3d2525d8ed9d'
url = 'https://api.themoviedb.org/3/authentication'
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
}
response = requests.get(url, headers=headers)

# Functions using API
def trending_movies(api_key):

    trend_url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
    }

    response = requests.get(trend_url, headers=headers)
    if response.status_code == 200:
        trend_movies = response.json()
        return trend_movies
    else:
        st.error("ERROR")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")
def trending_tv(api_key):
    trend_url = "https://api.themoviedb.org/3/trending/tv/day?language=en-US"


    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
    }

    response = requests.get(trend_url, headers=headers)
    if response.status_code == 200:
        trend_series = response.json()
        return trend_series
    else:
        st.error("ERROR")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")
def movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/={movie_id}/images?language=English"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        movie_image = response.json()
        return movie_image['backdrops'][0]
    else:
        st.error("ERROR")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")
def movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error("ERROR")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

def get_top(api_key):
    upcoming_url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"


    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTRkMzk0OTcyN2MzZDdjNDA0ZTNkMjUyNWQ4ZWQ5ZCIsIm5iZiI6MTcyMTc3NDY0OC43MjIxNjcsInN1YiI6IjY2YTAzMTdlOGU3NTk2YjdjN2JmNDMwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.htRUiBwH4fB8m5uqCTDsQasvLvDDPRKNaM-Z7ePedrs"
    }

    response = requests.get(upcoming_url, headers=headers)
    if response.status_code == 200:
        upcoming = response.json()
        return upcoming
    else:
        st.error("ERROR")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

# Formatting for Sidebar and Titles
st.title("🍿 The Movie Hub")
st.markdown("---")
st.sidebar.title("🍿 The Movie Hub")
category = st.sidebar.radio('Select your option:',
                                ("Home",
                                 "Trending",
                                 "Top Rated",
                                 "Compare"))

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

with st.sidebar.container(border=True):
    st.subheader("Sign up or log in:")
    username = st.text_input("Enter your username", key="username")
    password = st.text_input("Enter your password", key="password")
    click_me = st.button("Enter", disabled = False)
    if username and password:
        click_me = True
        if click_me:
            st.success("Thank you for registering")
            st.balloons()



# Home Landing Page:

if category == "Home":
    st.header("Welcome to The Movie Hub 🎉")

    st.header("Our Favorite Films")
    col1, col2, col3 = st.columns(3)
    with col1:
        poster_path = movie_details(299536)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("Avengers Infinity War")
    with col2:
        poster_path = movie_details(1895)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("Star Wars: Revenge of the Sith")
    with col3:
        poster_path = movie_details(601)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("E.T")

    col5, col6, col7 = st.columns(3)
    with col5:
        poster_path = movie_details(11036)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("The Notebook")
    with col6:
        poster_path = movie_details(105)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("Back to the Future")
    with col7:
        poster_path = movie_details(857)['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        st.image(image_url, use_column_width=True)
        st.caption("Saving Private Ryan")

    st.markdown("- - -")

    st.subheader("Active Users (Past 30 Days):")

    num_days = 30
    users = pd.DataFrame(np.random.randint(0, 200, size=(num_days, 1)), columns=['Users'])

    st.line_chart(data = users, x_label = "Day", y_label= "Users per Day")
    st.markdown("- - -")


    st.subheader("About Us")
    container = st.container(border=True)
    with st.container(border = True):
        st.write("Welcome to our movie insight platform, where cinema enthusiasts gather to explore, compare, and discover the world of movies. "
                    "Our mission is to provide comprehensive and up-to-date information on the latest films, helping you make informed viewing choices. "
                    "Whether you're looking for trending hits, in-depth ratings, or just a place to discuss your favorite movies, we've got you covered. "
                    "Our passion for movies drives us to deliver a seamless and engaging experience, making us your go-to destination for all things cinematic. "
                    "Join us and dive into the magic of movies!")
        st.subheader("Headquarters:")
        latitude = 25.7553898
        longitude = -80.3762833

        map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
        st.map(map_data, zoom=12)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Depending on sidebar selection, info is displayed

# Shows trending entertainment
if category == "Trending":
    trend = st.selectbox("Select your option:", ["", "Trending Movies", "Trending Shows"])
    if trend == "Trending Movies":

        trending_movies_dict = trending_movies(api_key)
        st.success("Trending movies loaded...")
        st.header("Trending Movies")

        # The table - - - - - - - - - - - - - - - - - - - - - - - - - - -

        show_table = st.checkbox("Display the Table")
        title_list = [movie['title'] for movie in trending_movies_dict['results']]
        date_list = [movie['release_date'] for movie in trending_movies_dict['results']]
        ratings_list = [movie['vote_average'] for movie in trending_movies_dict['results']]
        votes_list = [movie['vote_count'] for movie in trending_movies_dict['results']]

        df = pd.DataFrame(
            {
                "Title": title_list,
                "Release Date": date_list,
                "Vote Count": votes_list,
                "Rating": ratings_list,
            })

        if show_table:
            st.dataframe(df, column_config={
                "Title" : "Title",
                "Release Date" : "Release Date",
                "Vote Count" : st.column_config.NumberColumn("Vote Count"),
                "Rating" : st.column_config.NumberColumn("Rating", format = "%.2f ⭐")
            }, hide_index= True, use_container_width= True
                         )





        # Displaying the Movies - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        for movie in trending_movies_dict['results']:
            id = movie['id']
            movie_link = f"https://www.themoviedb.org/movie/{id}?language=en-US"
            poster_path = movie['poster_path']
            image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

            col1, col2 = st.columns(2)

            with col1:
                st.image(image_url)

            with col2:
                st.header(f"{movie['title']}")
                st.write(f"Release Date: {movie['release_date']}")
                st.write(f"Description: {movie['overview']}")

                st.link_button("Visit External Link", movie_link)

                # show_ranking = st.checkbox("Show Rating", value=False, key="show_ranking")
                # if show_ranking:
                #     rating = movie['vote_average']
                #     rating = round(rating, 1)
                #     st.write(f"Rating: {rating}")

            st.markdown("---")
    elif trend == "Trending Shows":

        st.success("Trending tv shows loaded...")
        st.header("Trending TV Shows")

        trending_shows_dict = trending_tv(api_key)

        show_table = st.checkbox("Display the Table")
        title_list = [movie['name'] for movie in trending_shows_dict['results']]
        date_list = [movie['first_air_date'] for movie in trending_shows_dict['results']]
        ratings_list = [movie['vote_average'] for movie in trending_shows_dict['results']]
        votes_list = [movie['vote_count'] for movie in trending_shows_dict['results']]

        df = pd.DataFrame(
            {
                "Title": title_list,
                "Release Date": date_list,
                "Vote Count": votes_list,
                "Rating": ratings_list,
            })

        if show_table:
            st.dataframe(df, column_config={
                "Title": "Title",
                "Release Date": "Release Date",
                "Vote Count": st.column_config.NumberColumn("Vote Count"),
                "Rating": st.column_config.NumberColumn("Rating", format="%.2f ⭐")
            }, hide_index=True, use_container_width=True
                         )


        for show in trending_shows_dict['results']:
            id = show['id']
            show_link = f"https://www.themoviedb.org/tv/{id}?language=en-US"
            poster_path = show['poster_path']
            image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

            col1, col2 = st.columns(2)

            with col1:
                st.image(image_url)

            with col2:
                st.header(f"{show['name']}")
                st.write(f"Release Date: {show['first_air_date']}")
                st.write(f"Description: {show['overview']}")

                st.link_button("Visit External Link", show_link)

                # show_ranking = st.checkbox("Show Rating")
                # if show_ranking:
                #     st.write(f"Rating: {show['vote_average']}")

            st.markdown("---")
    else:
        st.warning("Please select an option")

# Shows the top-rated films
elif category == "Top Rated":
    st.header("Top Rated of All Time:\n")
    st.write("")

    top_rated_dict = get_top(api_key)
    for movie in top_rated_dict['results']:

        id = movie['id']
        movie_link = f"https://www.themoviedb.org/movie/{id}?language=en-US"
        poster_path = movie['poster_path']
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

        col1, col2 = st.columns(2)

        with col1:
            st.image(image_url)

        with col2:
            st.header(f"{movie['title']}")
            st.write(f"Release Date: {movie['release_date']}")
            rounded = round(movie['vote_average'], 2)
            st.write(f"Rating: {rounded} 🎉")
            st.write(f"Description: {movie['overview']}")

            st.link_button("Visit External Link", movie_link)

        st.markdown("---")

# Uses charts to compare films
elif category == "Compare":
    st.header("Compare Movies")

    trending_movies_dict = trending_movies(api_key)
    top_rated_dict = get_top(api_key)
    title_list = [movie['title'] for movie in trending_movies_dict['results']] + [show['title'] for show in top_rated_dict['results']]
    rating_list = [movie['vote_average'] for movie in trending_movies_dict['results']] + [show['vote_average'] for show in top_rated_dict['results']]

    options = {}
    for i in range(len(title_list)):
        options[title_list[i]] = rating_list[i]

    selected = {}

    color = st.color_picker("Pick a color", "#FF0007")
    paramaters = st.multiselect("Select movies to compare", options.keys())



    if paramaters:
        st.success("Chart Loaded")
        selected = {title: options[title] for title in paramaters}

        st.bar_chart(data=selected,
                     use_container_width=True,
                     x_label="Rating",
                     y_label="Movies",
                     height = 800,
                     horizontal = True,
                     color = color
                     )
