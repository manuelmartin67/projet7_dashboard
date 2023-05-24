# projet7_dashboard
### Dashboard pour visualiser le score d'un client pour prêt bancaire

Ce dashboard fonctionne sous streamlit, et fait appel à des requêtes API sur projet7_flask https://projet7-flask.herokuapp.com/

## app.py
Ce fichier contient la structure de la page web.
On y retrouve la liste de sélection des ID clients

On a également les boutons de fonction pour :
- réaliser une modélisation
- afficher les infos du client
- afficher le graphe d'importance locale
- afficher le graphe d'importance globale
- afficher les graphes de comparaison de l'individu avec la population

Pour finir on trouve un slider permettant de choisir le nombre de features à afficher sur les graphes.

