""" core of the flask app"""
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
import json
from sklearn.neighbors import NearestNeighbors
from .visual import *
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    """splash page for those who may fall upon root directory, no planned
    functionality, but provide simple instructions on how to use app"""
    @app.route("/")
    # empty homepae used for testing
    def root():
        return """Welcome! Try /request/song id for song suggestions
                  or /visual/song id for visualizations"""
    """the route that returns the visual data for a requested song id in
    base64 format"""
    @app.route("/visual/<int:id>", methods=['POST', 'GET'])
    # returns the base64 value for a song visualization
    def visual(id):
        viz = base64_visualization(id)
        return viz

    """Accepts a song id and returns 10 suggested songs from our model"""
    @app.route("/request/<int:id>", methods=['POST', 'GET'])
    # returns song suggestion from Knearest Neighbor model
    def request(id):
        # load the pickled model and scaled data
        X = pickle.load(open('./data/X_scaled.pkl', 'rb'))
        loaded_model = pickle.load(open('./models/kn_model.pkl', 'rb'))

        # run the request through the model
        results = loaded_model.kneighbors([X[id]])[1]

        # change results from ndarray to list for json dumping
        test_r = results.tolist()
        tj = json.dumps({'results': test_r})

        return tj

    return app
