# Nos packages
import streamlit as st
import datetime

# New page
# Titre principal de l'application (affiché en haut de la page)
st.title("ADULTES via git")

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


if st.button("nm0000003"):
    st.session_state.selected_intervenant = "nm0000003"
    st.switch_page("pages/intervenant.py")
if st.button("nm0000079"):
    st.session_state.selected_intervenant = "nm0000079"
    st.switch_page("pages/intervenant.py")
