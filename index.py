# Nos packages
import streamlit as st
import pandas as pd
import datetime

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
st.title("🏠 ACTUELLEMENT EN SALLE 🌎")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Code pour telecharger le fichier csv
df = pd.read_csv("projet_2\data\data_movies_details.csv")

# On recupere les elements unique de la colonne pour les proposer en selection
sentiment_mapping = ["film pour enfant", "film pour adulte", "le casting"]

choix = st.selectbox("Veuillez faire votre sélection : ", sentiment_mapping)

# Suivant le choix de la personne, on afficher le type de film
if choix == 'film pour enfant':
    st.markdown(f"Vous avez choisi **{choix}** 🎈")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
        variable_test = "Origine : " + df.origin_country.unique()[i+7] + ". "
        "Overview : " + df.overview.unique()[i+7]
        left.image(df.poster_path.unique()[i+7], caption="poster_path")
        middle.image(df.backdrop_path.unique()[i+7], caption="backdrop_path")
        right.write(variable_test)
elif choix == 'film pour adulte':
    st.markdown(f"Vous avez choisi **{choix}** ⭐")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
        variable_test = "Origine : " + df.origin_country.unique()[i] + ". "
        "Overview : " + df.overview.unique()[i]
        left.image(df.poster_path.unique()[i], caption="poster_path")
        middle.image(df.backdrop_path.unique()[i], caption="backdrop_path")
        right.write(variable_test)
elif choix == 'le casting':
    st.markdown(f"Vous avez choisi **{choix}** 🌎")
    df = pd.read_csv("data_movies_details.csv")
    for i in range(3):
        left, middle, right = st.columns(3, border=True)
#       variable_1 = "https://image.tmdb.org/t/p/original"+(df.profile_path[i])
# Voir comment associer le debut de l'url et le profil-path
        variable_1 = "https://image.tmdb.org/t/p/original/" \
                     "ytMrG3T4SbZfZnfXFohjQBOixTQ.jpg"
        variable_2 = "Nom : " + df.name.unique()[i]
        # + "Statut : "+df.known_for_department.unique()[i]
        variable_3 = "Infos : " + df.known_for.unique()[i]
        left.image(variable_1, caption="p_path")
        middle.write(variable_2)
        right.write(variable_3)
else:
    st.write("Oui, ton choix est :", choix)

st.write('___')

st.write('Affichage du dataframe')
st.write(df)

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

st.write('© SAPEM Conseil')
