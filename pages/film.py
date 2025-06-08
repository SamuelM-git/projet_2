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

# Affichage par defaut
titre_du_film = "Film par defaut"

# -------- Load the data -------------
df_movies = pd.read_csv("data/films_final.csv")

#--------------- Selection film from carrousell-----------------
name = st.query_params.get("name", None)
st.write(name)

if name:
    st.session_state["selected_intervenant"] = name
    titre_du_film = "Film par defaut dans if"

if "selected_intervenant" not in st.session_state:
    st.session_state["selected_intervenant"] = "nm0000091" # A changer pour une film base

if st.session_state.selected_intervenant :
    tconst = st.session_state.selected_intervenant    
    df_inter = df_movies[df_movies['tconst'] == tconst]
    #titre_du_film = df_inter['title'].iloc[0]
    titre_du_film = df_inter['title'].iloc[0]

st.header(titre_du_film, divider="green")
st.write("La video")
st.video(df_inter.bande_annonce.iloc[0])
st.write("-------")
st.write("L'image backdrop")
st.image(df_inter.backdrop_path.iloc[0])
st.write("-------")
st.write("L'overview")
st.write(df_inter.overview.iloc[0])
st.write("-------")
st.write("L'image poster")
st.image(df_inter.poster_path.iloc[0])
st.write("-------")
st.write(df_inter)
st.write("-------")

if st.button("nm0000003"):
    st.session_state.selected_intervenant = "nm0000003"
    st.switch_page("pages/intervenant.py")
if st.button("nm0000079"):
    st.session_state.selected_intervenant = "nm0000079"
    st.switch_page("pages/intervenant.py")

st.divider()

