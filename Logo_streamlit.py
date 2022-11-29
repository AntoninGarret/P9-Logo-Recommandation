import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("MVP : Recommandation d'article pour la bibliothèque LOGO")


uid = st.text_input("Entrez votre identifiant utilisateur")

headers = {"Content-Type": "application/json"}

url = "https://logo-recommandation.azurewebsites.net/api/user/" + uid
#st.write("POST to url", uri)

try:
    resp = requests.post(url)
except:
    st.error("Failed to connect to the API")
if resp.text != "":
    if resp.text != "Found no user with this id":
        st.write("Articles recommandés : ", resp.text)
    else:
        st.write(resp.text)

