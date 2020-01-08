""" core of the flask app"""
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
import json
from sklearn.neighbors import NearestNeighbors
from .visual import *

#from flask_sqlalchemy import SQLAlchemy
#from .models import DB, Song_info

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data_acquisition/song_list.sqlite3'

#DB = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)

    @app.route("/")
    #empty homepae used for testing
    def root():
        return "this is the front page"

    @app.route("/visual/<int:id>", methods =['POST', 'GET'])
    #this was used testing
    def visual(id):
        viz = base64_visualization(id)
        return viz

    #add route to give jsonified data to backend team

    @app.route("/request/<int:id>", methods=['POST', 'GET'])
    def request(id):
        #id = request.args.get('id', default = 1, type = int)
        X = pickle.load(open('./data/X_scaled.pkl', 'rb'))
        loaded_model = pickle.load(open('./models/kn_model.pkl', 'rb'))
        results = loaded_model.kneighbors([X[id]])[1]
        test_r = results.tolist()
        tj = json.dumps({'results' : test_r})
        # print(request(1))
        return tj

    return app

    # if __name__=='__main__':
    #     app.debug=True
    #     app.run()
