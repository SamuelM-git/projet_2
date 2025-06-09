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

#Set page config -------------------------
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# Bar naviagation ----------------------------------
# Hide Streamlit UI
st.markdown("""
    <style>
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Make room for fixed nav */
        .block-container {
            padding-top: 40px;
        }

        /* Fixed top navbar */
        .topnav {
            position: fixed;
            top: 0;
            left: 120px;
            right: 120px
            width: 100%;
            background-color: #070E19;
            overflow: hidden;
            border-radius: 10px;
            z-index: 1000;
        }

        .topnav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 17px;
            border-radius: 10px;
        }

        .topnav a:hover {
            background-color: #06335E;
        }

        .topnav a.active {
            background-color: #062341;
        }
    </style>

    <div class="topnav">
        <a href="/" class="active" target="_self">Home</a>
        <a href="/Sugestion" target="_self">Sugestion</a>
        <a href="/Contacts" target="_self">Contacts</a>
        <a href="/enfants" target="_self">Enfants</a>
        <a href="/film" target="_self">Film</a>
    </div>
""", unsafe_allow_html=True)
#----------------------------------------------------


# Titre principal de l'application (affiché en haut de la page)
left, midel, right = st.columns([1,1.2,1])
midel.title("🏠 ACTUELLEMENT EN SALLE 🌎")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Code pour telecharger le fichier csv
df_movies = pd.read_csv("data/films_final.csv")
# ------------ Films en sale les dernier sortie anne 2024 + ---------
df_movies_filt = df_movies[(df_movies['startYear'] > 2023) & (df_movies['averageRating'] > 6)]
df_movies_filt = df_movies_filt.sort_values(by=['popularity'], ascending=False)
backdrop = df_movies_filt.backdrop_path.tolist()
col1, col2, col3, col4, col5, col6, col7 = backdrop[:7]
titles = df_movies_filt['title'].tolist()
title1, title2, title3, title4, title5, title6, title7 = titles[:7]


#Carousel doc https://pypi.org/project/st-ant-carousel/
from st_ant_carousel import st_ant_carousel

# Define the content with images
content = [
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content":f'<b2>{title1}</b2><img src="{col1}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title2}</b2><img src="{col2}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title3}</b2><img src="{col3}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title4}</b2><img src="{col4}" width="2000" height="700" style="cursor: pointer;">'
    },
    {
         "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title5}</b2><img src="{col5}" width="2000" height="700" style="cursor: pointer;">'
    },
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title6}</b2><img src="{col6}" width="2000" height="700">'
    },
    {
        "style": {"textAlign": "center", "color": "white", "fontSize": "50px"},
        "content": f'<b2>{title7}</b2><img src="{col7}" width="2000" height="700">'
    }
]

# Define carousel styling
carousel_style = {
    "width": "100%",
    "height": "700px",
    "background-color": "#12980300",
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
