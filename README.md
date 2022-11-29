# Projet 9

Ce projet est dédié à la conception et au déploiement d'une application de recommandation pour les articles de Globo.com

## Démarche à suivre pour compléter le déploiement
- Télécharger le [dataset](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/AI+Engineer/Project+9+-+R%C3%A9alisez+une+application+mobile+de+recommandation+de+contenu/news-portal-user-interactions-by-globocom.zip)
- Extraire le dataset dans le dossier _news-portal-user-interactions-by-globocom_
- créer un dossier _generated_files
- Exécuter le notebook _Recommandation_time.ipynb_ dans son intégralité
- déplacer les fichiers _article\_embeddings.pickle_ et _best-articles.json_ dans le dossier _AzureFunction/HttpLogoRec/_
- déployer la AzureFunction _HttpLogoRec_ sur Azure à l'aide de VScode
- mettre à jour l'url de la fonction dans _Logo\_streamlit.py_ 

## API déployée
L'API de recommandation est déployé à l'adresse [https://logo-recommandation.azurewebsites.net/api/user/](https://logo-recommandation.azurewebsites.net/api/user/). Compléter avec l'user_id désirée
Le fichier _Logo\_streamlit.py_  est une application simple qui fait appel à cet API. Avec streamlit installé, lancer avec streamlit run.