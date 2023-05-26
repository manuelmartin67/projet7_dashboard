import streamlit as st
import requests


st.title("Dashboard - Scoring client")

# Appeler votre API Flask pour obtenir la liste des ID clients
response = requests.get("https://projet7-flask.herokuapp.com/api/v1/data/id_clients/all")
id_clients = response.json()

# Extraire les valeurs des ID clients
id_values = [client["SK_ID_CURR"] for client in id_clients]

# Afficher la selectbox pour choisir l'ID client
selected_id = st.selectbox("Choisir l'ID client", id_values)


#url = f"https://projet7-flask.herokuapp.com/api/v1/model/id_clients?SK_ID_CURR={selected_id}"
#response = requests.get(url)
#results = response.json()
if "message" not in st.session_state :
    st.session_state.message = "En attente de modélisation"

# Afficher les résultats de la modélisation
st.header(st.session_state.message)

#resultat = "en attente"
# premier header
#head = st.header(resultat)

# Bouton pour exécuter la classification avec l'ID client sélectionné
#bouton_modelisation = st.sidebar.button("Exécuter la modélisation")
if st.sidebar.button("Exécuter la modélisation"):
    #Appeler votre API Flask avec l'ID client sélectionné pour effectuer la modélisation
    url = f"https://projet7-flask.herokuapp.com/api/v1/model/id_clients?SK_ID_CURR={selected_id}"
    response = requests.get(url)
    results = response.json()

    # Afficher les résultats de la modélisation
    st.session_state.message = results


# Bouton pour afficher les infos de l'ID client sélectionné
if st.sidebar.button("Afficher infos client"):
    # Appeler votre API Flask avec l'ID client sélectionné pour effectuer la modélisation
    url = f"https://projet7-flask.herokuapp.com/api/v1/data/id_clients?SK_ID_CURR={selected_id}"
    response = requests.get(url)
    results = response.json()

    # Afficher les infos
    st.write("Infos client :")
    st.write(results)

# Slider pour choisir le nombre de features à afficher
nb_features = st.sidebar.slider("Nombre de features",min_value=1,max_value=21,value=10)


# Bouton pour le graphe d'importance locale
if st.sidebar.button("Graphe d'importance locale"):
    # Appeler l'API Flask pour obtenir le graphe d'importance locale
    importance_local_url = f"https://projet7-flask.herokuapp.com/api/v1/model/id_clients/importance_locale?SK_ID_CURR={selected_id}&feature={nb_features}"
    importance_local_response = requests.get(importance_local_url)
    importance_local_graph = importance_local_response.text

    # Afficher le graphe d'importance locale
    st.write("Graphe d'importance locale :")
    st.components.v1.html(importance_local_graph, width=1000, height=800, scrolling=True)

# Bouton pour le graphe d'importance globale
if st.sidebar.button("Graphe d'importance globale"):
    # Appeler l'API Flask pour obtenir le graphe d'importance globale
    importance_global_url = f"https://projet7-flask.herokuapp.com/api/v1/model/id_clients/importance_globale?feature={nb_features}"
    importance_global_response = requests.get(importance_global_url)
    importance_global_graph = importance_global_response.text

    # Afficher le graphe d'importance globale
    st.write("Graphe d'importance globale :")
    st.components.v1.html(importance_global_graph, width=1000, height=800, scrolling=True)

# Bouton pour la comparaison avec la population
if st.sidebar.button("Comparaison avec la population"):
    # Appeler l'API Flask pour obtenir la comparaison avec la population de clients
    comparison_url = f"https://projet7-flask.herokuapp.com/api/v1/model/id_clients/comparaison?SK_ID_CURR={selected_id}&feature={nb_features}"
    comparison_response = requests.get(comparison_url)
    comparison_results = comparison_response.text

    # Afficher la comparaison avec la population de clients
    st.write("Comparaison avec la population de clients :")
    st.components.v1.html(comparison_results, width=1000, height=800, scrolling=True)

