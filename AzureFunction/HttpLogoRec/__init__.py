import logging

import azure.functions as func

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import json

def load_predictions(json_file):    
    with open(json_file, 'r') as f:
            str_pred = json.load(f)
    return str_pred

top_rated = load_predictions('HttpLogoRec/best_articles.json')
word_embed = pd.read_pickle('HttpLogoRec/articles_embeddings.pickle')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    uid = req.route_params.get('userid')

    if not uid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            uid = req_body.get('userid')

    if uid:
        if not uid in top_rated.keys():
         return func.HttpResponse("Found no user with this id")
        
        profile_article = word_embed[top_rated[uid]].mean(axis=0)
        sim = cosine_similarity(profile_article.reshape(1,-1), word_embed)[0]
        sim = np.argsort(sim)[-5:]
        return func.HttpResponse(str(sim))
    else:
        return func.HttpResponse("Pass a user id in the query string or in the request body for a recommandation")
