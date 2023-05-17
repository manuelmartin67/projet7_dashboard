import streamlit as st
import requests


st.title("Dashboard - Scoring client")

# Appeler votre API Flask pour obtenir la liste des ID clients
response = requests.get("http://127.0.0.1:5001/api/v1/data/id_clients/all")
id_clients = response.json()

# Extraire les valeurs des ID clients
id_values = [client["SK_ID_CURR"] for client in id_clients]

# Afficher la selectbox pour choisir l'ID client
selected_id = st.selectbox("Choisir l'ID client", id_values)

# Bouton pour exécuter la classification avec l'ID client sélectionné
if st.sidebar.button("Exécuter la modélisation"):
    # Appeler votre API Flask avec l'ID client sélectionné pour effectuer la modélisation
    url = f"http://127.0.0.1:5001/api/v1/model/id_clients?SK_ID_CURR={selected_id}"
    response = requests.get(url)
    results = response.json()

    # Afficher les résultats de la modélisation
    st.write("Résultats de la modélisation :")
    st.write(results)

# Slider pour choisir le nombre de features à afficher
nb_features = st.sidebar.slider("Nombre de features",min_value=1,max_value=21,value=10)

if st.sidebar.button("Graphe d'importance locale"):
    # Appeler votre API Flask pour obtenir le graphe d'importance locale
    importance_local_url = f"http://127.0.0.1:5001/api/v1/model/id_clients/importance_locale?SK_ID_CURR={selected_id}&feature={nb_features}"
    importance_local_response = requests.get(importance_local_url)
    importance_local_graph = importance_local_response.text

    # Afficher le graphe d'importance locale
    st.write("Graphe d'importance locale :")
    st.components.v1.html(importance_local_graph, width=1000, height=800, scrolling=True)

# Bouton pour le graphe d'importance globale
if st.sidebar.button("Graphe d'importance globale"):
    # Appeler votre API Flask pour obtenir le graphe d'importance globale
    importance_global_url = f"http://127.0.0.1:5001/api/v1/model/id_clients/importance_globale?feature={nb_features}"
    importance_global_response = requests.get(importance_global_url)
    importance_global_graph = importance_global_response.text

    # Afficher le graphe d'importance globale
    st.write("Graphe d'importance globale :")
    st.components.v1.html(importance_global_graph, width=1000, height=800, scrolling=True)

# Bouton pour la comparaison avec la population
if st.sidebar.button("Comparaison avec la population"):
    # Appeler votre API Flask pour obtenir la comparaison avec la population de clients
    comparison_url = f"http://127.0.0.1:5001/api/v1/model/id_clients/comparaison?SK_ID_CURR={selected_id}&feature={nb_features}"
    comparison_response = requests.get(comparison_url)
    comparison_results = comparison_response.text

    # Afficher la comparaison avec la population de clients
    st.write("Comparaison avec la population de clients :")
    st.components.v1.html(comparison_results, width=1000, height=800, scrolling=True)

