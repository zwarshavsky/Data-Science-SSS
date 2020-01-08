import pickle
import pandas as pd
from flask import jsonify
from sklearn.neighbors import NearestNeighbors

def predict(id):
    X = pickle.load(open('./data/X_scaled.pkl', 'rb'))
    loaded_model = pickle.load(open('./models/kn_model.pkl', 'rb'))
    results = loaded_model.kneighbors([X[id]])[1]
    return results

jsonify(predict(1))
#
# infile = open("kn_model.pkl",'rb')
# new_dict = pickle.load(infile)
# infile.close()
# print(new_dict)
# print(new_dict == kn_model)
# print(type(new_dict))
