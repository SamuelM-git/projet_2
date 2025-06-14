import numpy as np
import pandas as pd
import streamlit as st


#FastEmbed is a lightweight, fast, Python library built for embedding generation.
# https://github.com/qdrant/fastembed
# from fastembed import TextEmbedding

# Cosine_similarity -- Compute cosine similarity between samples in X and Y.
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer

#Load csv films
df_films = pd.read_csv('data/films_final.csv')



'''# Detecter les différents model qu'on peut utiliser
supported_models = (
    pd.DataFrame(TextEmbedding.list_supported_models())
    .sort_values("size_in_GB")
    .drop(columns=["sources", "model_file", "additional_files"])
    .reset_index(drop=True)
)

# print(supported_models.to_markdown())
st.write(supported_models)'''


#Print shape
df_films.shape


# Add sujestions.
# Add a row to the data frame.
def addsugestion(sugestion_title, sugenstion_genres, sugestion_words, sugestion_overview):
    sugestion_user = {'backdrop_path': 'Nothing', 'budget': 'Nothing', 'id' : 'Nothing', 'origin_country' : 'Nothing', 'overview' : sugestion_overview,
        'popularity': 'Nothing', 'poster_path' : 'Nothing', 'revenue' : 'Nothing', 'mots_cles': sugestion_words, 'title' : sugestion_title, 'tconst' :  'Nothing',
        'startYear' : 'Nothing', 'runtimeMinutes' : 'Nothing', 'genres' : sugenstion_genres, 'averageRating' : 'Nothing', 'numVotes' : 'Nothing',
        'bande_annonce' : 'Nothing'}
    df_films_sgestion = pd.concat([df_films, pd.DataFrame([sugestion_user])], ignore_index=True)
    return df_films_sgestion


# Aplication of sugestion

sugestion_title = st.text_input(f"sugestion_title : ")
sugenstion_genres = st.text_input(f"Sugenstion_genres : ")
sugestion_words = st.text_input(f'sugestion_words :')
sugestion_overview = st.text_input(f"sugestion_overview :")
if st.button("apply"):
    df_films = addsugestion(sugestion_title, sugenstion_genres, sugestion_words, sugestion_overview)
    st.session_state.df_films = df_films
    st.write(df_films.title.tail(5))


    #Treating data
    df_films['all_text'] = (
        "Genres : " + df_films['genres'] + ".\n"
        "Genres : " + df_films['genres'] + ".\n"
        "Mots_cles : " + df_films['mots_cles'] + ".\n"
        "Title : " + df_films['title'] + ".\n"
        "Overview : " + df_films['overview'] 
        
        )

    #Make a list of treated data
    st.session_state.documents = df_films['all_text'].to_list()

    df_films.tail(1)


#Funtion for model
# For sorme reason tqdm mmust be near the funtion to work...

if st.button("Generate Embeddings"):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(st.session_state.documents, show_progress_bar=True)
    st.session_state.embeddings = embeddings
    st.success("Embeddings generated.")

if st.button("Compute Distances"):
    if "embeddings" in st.session_state:
        distances = cosine_similarity(st.session_state.embeddings)
        df_distances = pd.DataFrame(distances)
        st.session_state.distances = df_distances
        st.success("Distances computed.")
    else:
        st.warning("Please generate embeddings first.")

'''#Function modele
def get_sim_embed(documents, name="BAAI/bge-small-en-v1.5"):
    
    embedding_model = TextEmbedding(model_name=name)
    
    # Show progress while generating embeddings
    embeddings_generator = list(embedding_model.embed(documents, desc="Embedding Documents"))
    
    # Compute cosine similarity between all embeddings
    # Returns the distance in np.array
    distance = cosine_similarity(embeddings_generator, embeddings_generator)
    
    # Transforme np.array into a DataFrame
    df_distance = pd.DataFrame(distance, index=range(len(documents)), columns=range(len(documents)))
    return df_distance

#Aplication of model and get distances
if st.button("Apply Distances"):
    if "documents" in st.session_state:
        distances = get_sim_embed(st.session_state.documents, "BAAI/bge-small-en-v1.5")
        st.session_state.distances = distances
        st.write("Distance matrix:")
        st.dataframe(distances)
    else:
        st.warning("No documents available — click 'Apply' first.")'''


#Find the recomendations
# Funtion to find the films returnning a url of the poster
def get_info_reco(title_input, max_reco = 5) :
    data = st.session_state.df_films
    distance_reco = st.session_state.distances
    
    # avoir la ligne contenant ma recette
    info_input = data[data.title== title_input]
    # récupérer l'index de l'input
    indice_input_index = info_input.index[0]
    #  recupérer la ligne de recommandation dans la matrice de distance
    scores = distance_reco.iloc[ indice_input_index ]

    #  trier de la valeur la plus haute à la plus basse
    scores  = scores.sort_values(ascending = False)


    # récuperer les indices de reco
    best_scores_index = scores.index.to_list()[1:max_reco+ 1]


    # récupérer les images des plats recmmandé

    st.write(f" pour le place {title_input}")
    st.write(info_input.poster_path.values[0])
    #indices_reco = np.argsort(scores)[::-1][1:]

    st.write(f' les recommandations : ')
    reco = data.iloc[best_scores_index]
    st.write(reco.poster_path.values)



# Test 
title = st.text_input(f"TITLE : ")
if st.button("Sugestion"):
    if "distances" in st.session_state:
        get_info_reco(title)
    else:
        st.warning("No documents available — click 'Apply' first.")
