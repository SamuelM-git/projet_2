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


# New page
# Titre principal de l'application (affiché en haut de la page)
st.title("ADULTES via git")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Le temps
# https://docs.streamlit.io/develop/api-reference/widgets/st.date_input
today = datetime.datetime.now()
st.write("Aujoud'hui nous sommes le :", today.date())

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Le placement
# https://docs.streamlit.io/develop/api-reference/layout/st.columns
left, middle = st.columns(2, vertical_alignment="bottom")

left.text_input("Entrez votre recherche :")
middle.button("valider", use_container_width=True)
# right.checkbox("Check me")

st.write('___')
# Titre principal de l'application (affiché en haut de la page)
st.title("FILM")
VIDEO_URL = "https://example.com/not-youtube.mp4"
st.video(VIDEO_URL)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Code pour telecharger les fichiers csv
df_data_movies_details = pd.read_csv("data/data_movies_details.csv")
df_film = pd.read_csv("data/films_final.csv")
df_intervenant = pd.read_csv("data/intervenantes_final.csv")
df_intervenant_1950 = pd.read_csv("data/intervenant_tmdb_find_by_ID_1950_r5.csv")

# Une affichage
left, middle, right = st.columns(3, border=True)
variable_test = "Origine : " + df_data_movies_details.origin_country.unique()[1] + ". "
"Overview : " + df_data_movies_details.overview.unique()[1]
left.image(df_data_movies_details.poster_path.unique()[1], caption="poster_path")
middle.image(df_data_movies_details.backdrop_path.unique()[1], caption="backdrop_path")
right.write(variable_test)

st.write('___')

import numpy as np
# La atble
tab1, tab2, mtab = st.tabs(["📈 Intervenants", "🗃 Data", "Graphique"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

mtab.subheader("A tab with a chart")
mtab.write(df_intervenant.birthYear)

st.write('___')

# On recupere les elements unique de la colonne pour les proposer en selection
sentiment_mapping = ["film pour enfant", "film pour adulte", "le casting"]

choix = st.selectbox("Veuillez faire votre sélection : ", sentiment_mapping)

# Suivant le choix de la personne, on afficher le type de film
if choix == 'film pour enfant':
    st.markdown(f"Vous avez choisi **{choix}** 🎈")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
        variable_test = "Origine : " + df_data_movies_details.origin_country.unique()[i+7] + ". "
        "Overview : " + df_data_movies_details.overview.unique()[i+7]
        left.image(df_data_movies_details.poster_path.unique()[i+7], caption="poster_path")
        middle.image(df_data_movies_details.backdrop_path.unique()[i+7], caption="backdrop_path")
        right.write(variable_test)
elif choix == 'film pour adulte':
    st.markdown(f"Vous avez choisi **{choix}** ⭐")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
        variable_test = "Origine : " + df_data_movies_details.origin_country.unique()[i] + ". "
        "Overview : " + df_data_movies_details.overview.unique()[i]
        left.image(df_data_movies_details.poster_path.unique()[i], caption="poster_path")
        middle.image(df_data_movies_details.backdrop_path.unique()[i], caption="backdrop_path")
        right.write(variable_test)
elif choix == 'le casting':
    st.markdown(f"Vous avez choisi **{choix}** 🌎")
    df_data_movies_details = pd.read_csv("data_movies_details.csv")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
#       variable_1 = "https://image.tmdb.org/t/p/original"+(df_data_movies_details.profile_path[i])
# Voir comment associer le debut de l'url et le profil-path
        variable_1 = "https://image.tmdb.org/t/p/original/" \
                     "ytMrG3T4SbZfZnfXFohjQBOixTQ.jpg"
        variable_2 = "Nom : " + df_data_movies_details.name.unique()[i]
        # + "Statut : "+df_data_movies_details.known_for_department.unique()[i]
        variable_3 = "Infos : " + df_data_movies_details.known_for.unique()[i]
        left.image(variable_1, caption="p_path")
        middle.write(variable_2)
        right.write(variable_3)
else:
    st.write("Oui, ton choix est :", choix)

st.write('___')

st.write('Affichage du dataframe 1 - df_data_movies_details')
st.write(df_data_movies_details)

st.write('___')

st.write('Affichage du dataframe 2 - df_film')
st.write(df_film)

st.write('___')

st.write('Affichage du dataframe 3 - df_intervenant')
st.write(df_intervenant)

st.write('___')

st.write('Affichage du dataframe 4 - df_intervenant_1950')
st.write(df_intervenant_1950)

st.write('___')


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Les feedback
# https://docs.streamlit.io/develop/api-reference/widgets/st.feedback
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")


st.write(' 🦁 ')
