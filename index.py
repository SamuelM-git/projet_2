# Nos packages
import streamlit as st
import pandas as pd

# New page
# Titre principal de l'application (affiché en haut de la page)
st.title("ACTUELLEMENT EN SALLE")

st.button("Enfants")
st.button("Adultes")
st.button("Castings")

# Code pour telecharger le fichier csv
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/"
                 "seaborn-data/master/taxis.csv")

# On recupere les elements unique de la colonne pour les proposer en selection
choix = st.selectbox("Indiquez votre arrondissement de récupération",
                     df.pickup_borough.unique())
st.write('___')

st.write("Tu as choisi:", choix)

# Suivant le choix de la personne, on affiche la photo correspondante
if choix == 'Bronx':
    st.image("image/bronx.png")
elif choix == 'Brooklyn':
    st.image("image/brooklyn.png")
elif choix == 'Manhattan':
    st.image("image/Manhattan.png")
elif choix == 'Queens':
    st.image("image/queens.png")
# Pas besoin de tester le cas avec nan car c'est le cas par defaut
else:
    st.image("image/nan.png")

st.write('___')

st.write(' 🦁 ')
