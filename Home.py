# Nos packages
import streamlit as st
import pandas as pd
import datetime
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # , MinMaxScaler
from sklearn.neighbors import NearestNeighbors
# Search box need to pip install streamlit_searchbox
# Makes a search box for title de filme
from streamlit_searchbox import st_searchbox
from streamlit_carousel import carousel
st.set_page_config(layout="wide")


# Titre principal de l'application (affiché en haut de la page)
st.title("🏠 ACTUELLEMENT EN SALLE 🌎")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Code pour telecharger le fichier csv
df_movies = pd.read_csv("data/films_final.csv")
# ------------ Films en sale les dernier sortie anne 2024 + ---------
df_movies_an2024 = df_movies[(df_movies['startYear'] > 2023) & (df_movies['averageRating'] > 6)]

backdrop = df_movies_an2024.backdrop_path.tolist()
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = backdrop[:10]



#Carousel doc https://pypi.org/project/st-ant-carousel/
import streamlit as st
from st_ant_carousel import st_ant_carousel

# Define the content with images
content = [
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col1}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col2}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col3}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col4}" width="2000" height="700" style="cursor: pointer;">'
    },
    {
         "style": {"textAlign": "center"},
        "content": f'<img src="{col5}" width="2000" height="700" style="cursor: pointer;">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col6}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col7}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col8}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{col9}" width="2000" height="700" style="cursor: pointer;">'
    },
    {
         "style": {"textAlign": "center"},
        "content": f'<img src="{col10}" width="2000" height="700" style="cursor: pointer;">'
}
]

# Define carousel styling
carousel_style = {
    "width": "100%",        # set desired width
    "height": "700px",       # optional height
    "margin": "0 auto",      # center the carousel
    "background-color": "#119803",
    "border": "0px solid #ccc",
    "border-radius": "0px",
    "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "padding": "0px"
}

# Display the carousel


st_ant_carousel(
    content,
    carousel_style=carousel_style,
    autoplay=True,
    autoplaySpeed=2000,
    dotPosition="bottom",
    dots=True,
    waitForAnimate=True,
    easing="ease-in-out",
    effect="scrollx",
    pauseOnDotsHover=True,
    pauseOnHover=True,
    animationSpeed=2000,
    vertical=False,
    adaptiveHeight=True, 
    height=700
)
