# Nos packages
import streamlit as st
import datetime

# ------ set page config ----------
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

## Bar naviagation ----------------------------------
# Hide Streamlit UI
st.markdown("""
    <style>
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Make room for fixed nav */
        .block-container {
            padding-top: 40px;
        }

        /* Fixed top navbar */
        .topnav {
            position: fixed;
            top: 0;
            left: 100px;
            width: 100%;
            background-color: #070E19;
            overflow: hidden;
            z-index: 1000;
        }

        .topnav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 17px;
            border-radius: 10px
        }

        .topnav a:hover {
            background-color: #06335E;
        }

        .topnav a.active {
            background-color: #062341;
        }
    </style>

    <div class="topnav">
        <a href="/" target="_self">Home</a>
        <a href="/Sugestion" target="_self">Sugestion</a>
        <a href="/Contacts" target="_self">Contacts</a>
        <a href="/enfants"  class="active" target="_self">Enfants</a>
        <a href="/film" target="_self">Film</a>
    </div>
""", unsafe_allow_html=True)
#----------------------------------------------------

# New page
# Titre principal de l'application (affiché en haut de la page)
st.title("ENFANTS")

# Les pages :
with st.container():
    # https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page
    # if st.button(label="Home", icon="🏠"):
    if st.button("Home"):
        st.switch_page("index.py")
    if st.button("Enfants"):
        st.switch_page("pages/enfants.py")
    if st.button("Adultes"):
        st.switch_page("pages/adultes.py")
    if st.button("Castings"):
        st.switch_page("pages/castings.py")

# Les pages
# st.page_link("index.py", label="Home", icon="🏠")
# st.page_link("pages/enfants.py", label="Enfants", icon="1️⃣")
# st.page_link("pages/adultes.py", label="Adultes", icon="1️⃣")
# st.page_link("pages/castings.py", label="Castings", icon="2️⃣",
# disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Le temps
# https://docs.streamlit.io/develop/api-reference/widgets/st.date_input
today = datetime.datetime.now()
st.write("Aujoud'hui nous sommes le :", today)
