import pandas as pd
import streamlit as st


#------------- Load data frame and show if needed------------
df_movies = pd.read_csv("data/films_final.csv")
df_movies

'''#---------------- Load page --------------------------------
df_movies = pd.read_csv("data/films_final.csv")

# -------- Get the film ID from the query params -------------
film_id = st.query_params.get("name", [None])[0]

# -------- Set session state if the film_id is found ----------
if film_id:
    st.session_state["selected_film"] = film_id

# -------- Lookup the film in the DataFrame ----------
tconst = st.session_state.get("selected_film")

if tconst:
    df_selected = df_movies[df_movies["tconst"].str.contains(tconst)]

    if not df_selected.empty:
        # Show the correct title
        st.header(df_selected["title"].iloc[0], divider="green")

        # Optional: show more info
        st.write(df_selected.iloc[0])
    else:
        st.warning("Film not found in the dataset.")
else:
    st.warning("No film ID provided in query parameters.")
'''

#--------------- Selection film from carrousell-----------------
name = st.query_params.get("name", None)

if name:
    st.session_state["selected_intervenant"] = name

if "selected_intervenant" not in st.session_state:
    st.session_state["selected_intervenant"] = "nm0000091" # A changer pour une film base

tconst = st.session_state.selected_intervenant    
df_inter = df_movies[df_movies['tconst'] == tconst]


st.header(df_inter['title'].iloc[0], divider="green")