# Nos packages
import streamlit as st
from datetime import datetime
from PIL import Image # il sert à ouvrir les images dans streamlit
import pandas as pd
import os # gérer des fichiers et des chemins dans mon ordi.  il sert de vérifier un fichier existant, créer des dossiers

# la page de contact de notre application streamlit

#--------------------mettre le logo
logo = Image.open(r"E:\STREAMLIT_PROJET2_FINAL\projet_2\pages\assets\image SAPEM.png")  # le chemin de l'image de notre logo
st.image(logo, width=50) # paramètre du logo
#-------En-tête avec bouton à droite et Titre principal de l'application (affiché en haut de la page)

# --- Initialisation de l'état ---
if "popup_active" not in st.session_state:
    st.session_state["popup_active"] = False

# Initialiser les champs lors que l'utilisateur vient écrire le message
if "nom" not in st.session_state:
    st.session_state.nom = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "message" not in st.session_state:
    st.session_state.message = ""
# -----------En-tête-----------------------------
st.title("🎬 Contactez l'équipe") # le titre de notre formulaire

# nous avons créer les colonnes pour mettre le bouton à droite car nous n'utilisaons pas html dans streamlit
# -----------colonne titre + bouton ----------------

col1, col2 = st.columns([5,3]) # nous ajustons les largeurs, plus large à gauche pour le titre
#--------------Création du bouton pour afficher le formulaire

with col2:
    if st.button("📬 Écrire un message"):
        st.session_state["popup_active"] = True
# ---------------------------------------------------

# -----------------------------style CSS du popup

st.markdown(
    """
    <style>
    .popup-style {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True  
            )
#--------------------------------------------
# --- Affichage du formulaire popup si bouton cliqué ---
# conteneur centré pour simuler un po-up car streamlit ne fait pas de popup comme sur java script ou html

if st.session_state["popup_active"]:

# centrons avec les colonnes 
    col_empty, col_popup, col_empty2 = st.columns([1,2,1])
    with col_popup:
        st.markdown('<div class="popup-style">', unsafe_allow_html=True)
        with st.form(key="formulaire_popup"):
            st.markdown("### 📝 Envoyer un message")
            st.session_state.nom = st.text_input("Nom", value=st.session_state.nom)
            st.session_state.email = st.text_input("Email", value=st.session_state.email)
            st.session_state.message = st.text_area("Message", value=st.session_state.message)

            submit = st.form_submit_button("Envoyer")

            if submit:
                # si envoyer, enrégistrer les informations dans le CSV
                 if st.session_state.nom and st.session_state.email and st.session_state.message:
                    nouvelle_ligne = {
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "nom": st.session_state.nom,
                        "email": st.session_state.email,
                        "message": st.session_state.message
                    }
# ---------------------stockons les informations dans un csv
                    dossier_csv = "data_contacts"
                    fichier_csv = os.path.join(dossier_csv,"Contacts.csv")
                    if not os.path.exists(dossier_csv):
                        os.makedirs(dossier_csv)
                        pd.DataFrame(columns=["date", "nom", "email", "message"]).to_csv(fichier_csv, index=False)

                    df = pd.read_csv(fichier_csv)
                    df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
                    df.to_csv(fichier_csv, index=False)

                    st.success("✅ Merci pour votre message !")
                
#------------------------------------Réinitialiser les champs
                    st.session_state.nom = ""
                    st.session_state.email = ""
                    st.session_state.message = ""
#-------------------fermer le formulaire -------------
                
                    st.session_state["popup_active"] = False # Masquer le formulaire après avoir envoyé
        
                # Fermer le formulaire et revenir à la page principale
                    st.rerun()
                # sinon affiche un message d'erreur
            else:
                    st.warning("⚠️ Merci de remplir tous les champs.")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------



# --------------Titre du formulaire ---------------------------
with col1:
    st.markdown("###" )  # espace pour le titre

# -----------------------    

# ---------------------------------------
st.write("""
Vous avez une question, une suggestion ou un bug à signaler ?  
N'hésitez pas à nous contacter !

### 👥 Notre Équipe Projet

- 👨‍💼 **Samir** — *Data Analyst*  
- 📊 **Pédro** — *Product Owner*  
- 👩‍💻 **Marie Claude** — *Data Analyst*  
- 👨‍💻 **Samuel** — *Développeur*  
- 🧭 **Lylle Audrey** — *Scrum Master*
         
""")
# --------------------------------------
# --- Affichage titres ---

st.markdown('<div class="title">Contactez-nous</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">SAPEM CONSEIL - Experts en stratégie et données</div>', unsafe_allow_html=True)

# ------------------------------
st.markdown("---")
# -------------------------------------------------------
# ------ pour le remplissage du formulaire de contact principale----------------


#---------------affichage du formulaire--------------------
st.markdown("### 📝 Laissez-nous un message")

with st.form("formulaire_contact"):
    nom = st.session_state.nom = st.text_input("Nom", value=st.session_state.nom)
    email = st.session_state.email = st.text_input("Email", value=st.session_state.email)
    message = st.session_state.message = st.text_area("Message", value=st.session_state.message)

    bouton_envoyer = st.form_submit_button("Envoyer")

    if bouton_envoyer:
        if nom and email and message:
            st.success("✅ Merci pour votre message! Nous vous répondrons rapidement.")
           # (nous allons enrégistrer dans un CSV ici)
        else:
            st.warning("⚠️ Merci de remplir tous les champs avant d'envoyer.")

# ----------------------------------------

# --------------pour stocker chaque message envoyer dans un csv----------
if bouton_envoyer:
        if nom and email and message: # si l'utilisateur a cliqué sur le bouton envoyé après avoir tout bien rempli les espaces demandées
            # Préparer les données
            date_envoi = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # la date du jour
            nouvelle_ligne = {
                "date": date_envoi,
                "nom": nom,
                "email": email,
                "message": message
            }

            # Créons le fichier s'il n'existe pas
            dossier_csv = "data_contacts"
            fichier_csv = os.path.join(dossier_csv,"Contacts.csv")
            if not os.path.exists(dossier_csv):
                os.makedirs(dossier_csv)
                df_init = pd.DataFrame(columns=["date", "nom", "email", "message"])
                df_init.to_csv(fichier_csv, index=False)

            # Ajoutons la ligne au fichier
            df = pd.read_csv(fichier_csv)
            df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
            df.to_csv(fichier_csv, index=False)

#-------------------------------
#--------- Réinitialisation des champs
            st.session_state["nom"] = ""
            st.session_state["email"] = ""
            st.session_state["message"] = ""
#-------------------------------------------------------

# ----------------------Infos de contact avec icônes
st.markdown("""
### 📧 Email  
contact@sapemconseil.com

### 📞 Téléphone  
+33 1 00 00 00 00

### 📍 Adresse  
15 rue 3 Fontaines 70240 La Creuse   
""")

#---------------------------------------------

# --- bas de page ---
st.markdown('<div class="footer">© 2025 SAPEM CONSEIL. Tous droits réservés.</div>', unsafe_allow_html=True)

# --- Styles personnalisés de notre page de contact ---
st.markdown("""
    <style>
    .main {
        background-color: #EFF5F3;
    }
    .title { 
        color: #0B2C4A;
        font-size: 36px;
        text-align: center;
        font-family: 'Georgia';
        margin-bottom: 10px;
    }
    .subtitle {
        color: #00C5A2;
        font-size: 20px;
        text-align: center;
        font-family: 'Verdana';
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 14px;
        color: #A0A0A0;
    }
    </style>
""", unsafe_allow_html=True)
# -------

#--------------style du bouton du formulaire
st.markdown("""
<style>
    .stButton>button {
        background-color: #ffcc00;
        color: black;
        border-radius: 12px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------