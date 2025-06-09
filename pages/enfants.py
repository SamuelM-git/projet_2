# Nos packages
import streamlit as st
import datetime
from streamlit_option_menu import option_menu

# ------ set page config ----------
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

## Bar naviagation ----------------------------------
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Sugestion", "Contacts", "Enfants", "Film"],
        icons=[],  # No icons
        default_index=3,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#05335F",
                "class": "navbar-fixed",  # Add fixed class
            },
            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "margin": "0px",
                "padding": "10px",
            },
            "nav-link-selected": {
                "background-color": "#1B4F72"
            },
        }
    )

if selected == "Home":
    st.switch_page("index.py")
if selected == "Sugestion":
    st.switch_page("pages/Sugestion.py")
if selected == "Contacts":
    st.switch_page("pages/Contacts.py")
if selected == "Enfants":
    selected = "Enfants"


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
