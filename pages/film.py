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
df_intervenant = pd.read_csv("data/intervenantes_final.csv")
df_intervenant_1950 = pd.read_csv("data/intervenant_tmdb_find_by_ID_1950_r5.csv")

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

st.header("Titre du film : "+titre_du_film, divider="green")
st.video(df_inter.bande_annonce.iloc[0])
st.write("-------")
# Le bloc de 3 parties de présentation : l'affiche, le resume et les autres infos
#resume_film = df_inter.overview.iloc[0]
#infos_film = "Populaité : "+str(df_inter.popularity.iloc[0])+"\nAnnée de sortie : "+str(df_inter.startYear.iloc[0])+"\nGenre : "+df_inter.genres.iloc[0]+"\nScore : "+str(df_inter.averageRating.iloc[0])+" sur "+str(df_inter.numVotes.iloc[0])+" votant(s)."
left, middle, right = st.columns(3, border=True)
left.image(df_inter.poster_path.iloc[0], caption="l'affiche")
middle.write("Résumé :")
middle.write(df_inter.overview.iloc[0])
right.write("Popularité : "+str(df_inter.popularity.iloc[0]))
right.write("Année de sortie : "+str(df_inter.startYear.iloc[0]))
right.write("Genre : "+df_inter.genres.iloc[0])
right.write("Score : "+str(df_inter.averageRating.iloc[0])+" sur "+str(df_inter.numVotes.iloc[0])+" votant(s)")
st.write("-------")


"""
 for i in range(100):
     if df_intervenant.knownForTitles.iloc[i].isin(df_inter.popularity.iloc[0]) :
         left, middle, right = st.columns(3, border=True)
         left.image(df_intervenant.poster_path.iloc[i], caption=df_intervenant.primaryName.iloc[0)
         middle.image(df_intervenant.poster_path.iloc[i], caption="backdrop_path")
         right.write("Test en cours")
st.write("-------")
"""
if st.button("nm0000003"):
    st.session_state.selected_intervenant = "nm0000003"
    st.switch_page("pages/intervenant.py")
if st.button("nm0000079"):
    st.session_state.selected_intervenant = "nm0000079"
    st.switch_page("pages/intervenant.py")

st.divider()

