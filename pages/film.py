import pandas as pd
import streamlit as st


#------------- Load data frame and show if needed------------
df_movies = pd.read_csv("data/films_final.csv")
df_movies

#--------------- Selection film from carrousell-----------------
name = st.query_params.get("name", None)

if name:
    st.session_state["selected_intervenant"] = name



tconst = st.session_state.selected_intervenant    
df_inter = df_movies[df_movies['tconst'] == tconst]


st.header(df_movies['title'].iloc[0], divider="green")


st.switch_page("movies")