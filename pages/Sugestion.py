import pandas as pd
import streamlit as st
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # , MinMaxScaler
from sklearn.neighbors import NearestNeighbors
# Search box need to pip install streamlit_searchbox
# Makes a search box for title de filme
from streamlit_searchbox import st_searchbox
from streamlit_carousel import carousel

# Titre de la page
st.title("Choisir un film")
st.write('Choisir votre filme favorite dans le genre comedie de production francaise')

# Load data frame and show if needed:
df_movies = pd.read_csv("data/films_final.csv")
# st.write(df_movies)
dummies = df_movies.genres.str.get_dummies(sep=',').drop(columns="Comedy")
genres = dummies.columns.to_list()
df_movies = pd.concat([df_movies, dummies], axis=1)

cols = ['budget', 'revenue', 'popularity', 'startYear', 'runtimeMinutes',
        'averageRating', 'numVotes'] + genres


# Function sugestion de filme:
def recherche(tconst, cols):

    # colonne ml

    # Defenir les X_class en colluns
    X_class = df_movies[cols]

    # Indiquer le filme au model
    X_test_c = df_movies.loc[df_movies["tconst"] == tconst, cols]

    # Standardiser toutes ces features
    scaler_knn = StandardScaler()
    X_knn_scaled = scaler_knn.fit_transform(X_class)

    # Nombre de voisins à trouver k et indiquer le numero de recumendations
    k = 5
    nn_model = NearestNeighbors(n_neighbors=k).fit(X_knn_scaled)

    # Standardiser toutes ces features
    X_test_c_scaled_knn = scaler_knn.transform(X_test_c)

    # Sélectionner les 3 premiers points de X_test_c (qui sont non
    # standardisés)
    sample_points_scaled = X_test_c_scaled_knn[:3, :]

    # .kneighbors() prend les points standardisés et retourne distances et
    # indices
    distances, indices = nn_model.kneighbors(sample_points_scaled)

    # Find the index
    indicies = indices[0].tolist()

    return df_movies.iloc[indicies]


# Funtion to search the title of filme in the dataframe:
def search_film(searchterm):
    # Search for the searchterm
    results = df_movies[df_movies["title"].str.contains(searchterm, case=False,
                                                        na=False)]
    return results["title"].tolist()


# Search function from streamlit_searchbox and disgn of the box search
selected_value = st_searchbox(
    search_film,
    placeholder="Search Film... ",
    # Text in the search box if nothing inside
    # key="my_key", #No parametre info
)

# If nothing in search box "selected_value' the return of carrousel is
# controled here:
film_id = df_movies[df_movies["title"].str.contains(
    "Le plaisir" if not isinstance(selected_value, str) else selected_value)]

# Acess the links of poster films
df_sugest = recherche(film_id["tconst"].iloc[0], cols)
for i, k in enumerate(df_sugest['poster_path']):
    if i == 0:
        img1 = k
    elif i == 1:
        img2 = k
    elif i == 2:
        img3 = k
    elif i == 3:
        img4 = k
    elif i == 4:
        img5 = k

img4title = film_id['title'].iloc[0]

# Show the value input on the searchbox



#Funtion link
#def chosenlink(linkid):
#    st.session_state.selected_intervenant = linkid


#Carousel doc https://pypi.org/project/st-ant-carousel/
import streamlit as st
from st_ant_carousel import st_ant_carousel

# Define the content with images
content = [
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{img1}" width="450" height="800">'"<b>2. Entry</b>"
    },
    {
        "style": {"textAlign": "center"},
        "content": f'<img src="{img2}" width="450" height="800">'"<b>2. Entry</b>"
    },
    {
        "style": {"textAlign": "center"},
        "content": f"""
            <div style="padding: 10px;">
                <img src="{img3}" width="450" height="800">
            </div>
        """
    },
    {
        "style": {"textAlign": "center"},
        "content": f'''
            <div>
                <a href="https://www.imdb.com/title/tt1375666/" target="_blank">
                    <img src="{img4}" width="450" height="500">
                </a>
                <h3>Inception</h3>
                <p>Open IMDb page in new tab</p>
            </div>
        '''
    },
{
    "style": {"textAlign": "center"},
    "content": f"""
        <div style="padding: 10px; text-align: center;">
            <a href="https://projet2-fcxec4iqdogknwxmwsamtt.streamlit.app/film?name=tt0044602" 
               target="_blank" 
               style="text-decoration: none; display: inline-block;">
                <img src="{img5}" width="450" height="750" style="cursor: pointer;">
            </a>
        </div>
    """
}
]

# Define carousel styling
carousel_style = {
    "width": "500px",        # set desired width
    "height": "800px",       # optional height
    "margin": "0 auto",      # center the carousel
    "background-color": "#f0f2f5",
    "border": "2px solid #ccc",
    "border-radius": "8px",
    "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "padding": "5px"
}

# Display the carousel
selected_index = st_ant_carousel(
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
    animationSpeed=500,
    vertical=False,
    adaptiveHeight=True, 
    height=800
)

#if selected:
#   st.session_state["selected_intervenant"] = selected['title']
#    st.switch_page("pages/intervenant.py")


# Show the carousel and get selected index
#selected_index = st_ant_carousel(slides, height=350)


for i, f in enumerate(df_sugest['title']):
    if i == 0:
        title1 = f
    elif i == 1:
        title2 = f
    elif i == 2:
        title3 = f
    elif i == 3:
        title4 = f
    elif i == 4:
        title5 = f

for i, t in enumerate(df_sugest['tconst']):
    if i == 0:
        tconts1 = t
    elif i == 1:
        tconts2 = t
    elif i == 2:
        tconts3 = t
    elif i == 3:
        tconts4 = t
    elif i == 4:
        tconts5 = t

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button(f"{title2}"):
        st.session_state.selected_intervenant = tconts2
        st.switch_page("pages/film.py")
with col2:
    if st.button(f'{title3}'):
        st.session_state.selected_intervenant = tconts3
        st.switch_page("pages/film.py")
with col3:
    if st.button(f'{title4}'):
        st.session_state.selected_intervenant = tconts4
        st.switch_page("pages/film.py")
with col4:
    if st.button(f"{title5}"):
        st.session_state.selected_intervenant = tconts5
        st.switch_page("pages/film.py")
