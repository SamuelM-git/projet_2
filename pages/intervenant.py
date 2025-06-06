import streamlit as st
import pandas as pd
import requests

df_inter = pd.read_csv('data/intervenantes_final.csv')

# Show the dataframe to explorer
# st.write(df_inter)

# Variable persona chose the intervenant
persona = "nm0000003"
df_inter = df_inter[df_inter['nconst'] == persona]


st.header('Intervenants')
st.divider()

# Def 2 col in intervenant
col1, col2 = st.columns(2)


# Col1 intervenant
col1.image(df_inter['profile_photo'].iloc[0])


# Col2 intervenant
# Preparation text to descrive intervenant
if df_inter['deathYear'].isna is True:
    dead = "Elle est décédée le " + {int(df_inter['deathYear'].iloc[0])} + "."
else:
    dead = "."

if df_inter['place_of_birth'].iloc[0] == "inconnue":
    place = "dans la ville " + df_inter['place_of_birth'].iloc[0]
else:
    place = "dans une ville " + df_inter['place_of_birth'].iloc[0]


texte = (f"""{df_inter['primaryName'].iloc[0]},
        né(e) le {int(df_inter['birthYear'].iloc[0])}
        {place}, était un intervenante reconnue dans le domaine du {
            df_inter['known_for_department'].iloc[0]}.
        {dead}""")


col2.header(df_inter['primaryName'].iloc[0], divider="green")
col2.markdown("""<style>.big-font {font-size:20px !important;}</style>""",
              unsafe_allow_html=True)
col2.markdown(f'<p class="big-font">{texte}</p>', unsafe_allow_html=True)


tab1, tab2 = st.tabs(["Biography", "Autres films"])

with tab1:
    st.header("Biography", divider="green")
    st.write(df_inter['biography'].iloc[0])

with tab2:

    col1, col2, col3, col4 = st.columns(4)

    # GraphQL endpoint
    url = "https://graph.imdbapi.dev/v1"

    # GraphQL query with variable
    query = """
    query exampleMultiTitleIDsx($ids: [String!]!) {
    titles(ids: $ids) {
        id
        primary_title
        original_title
        posters {
        url
        width
        height
        }
    }
    }
    """

    # IDs from DataFrame
    imdb_ids = df_inter['knownForTitles'].iloc[0].split(',')
    variables = {"ids": imdb_ids}
    # st.write(f"imdb ids {imdb_ids}")

    # Send the request
    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )

    # Results lists
    result_title = []
    result_poster = []

    # Json
    if response.status_code == 200:
        data = response.json()
        titles = data.get("data").get("titles")
        # st.write("Titres récupérés :", titles)

        for title in titles:
            if bool(title.get('original_title')) is True:
                result_title.append(title.get('original_title'))
                posters = title.get("posters")
                if posters:
                    result_poster.append(posters[0].get('url'))
                else:
                    result_poster.append("projet_2/assets/no_poster.jpg")
            else:
                result_title.append(title.get('primary_title'))
                posters = title.get("posters")
                if posters:
                    result_poster.append(posters[0].get('url'))
                else:
                    result_poster.append("projet_2/assets/no_poster.jpg")

        # Show
        # st.write(f"films {result_title}")
        # st.write(f"poster {result_poster}")

    else:
        st.write("❌ Requête échouée :", response.status_code)
        st.write(response.text)  # pour diagnostiquer l'erreur      

    col1.write(result_title[0])
    col2.write(result_title[1])
    col3.write(result_title[2])
    col4.write(result_title[3])

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.image(result_poster[0])
    col2.image(result_poster[1])
    col3.image(result_poster[2])
    col4.image(result_poster[3])
