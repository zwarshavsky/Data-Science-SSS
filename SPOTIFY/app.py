""" core of the flask app"""
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle
import json
from sklearn.neighbors import NearestNeighbors


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

    @app.route("/search")
    #this was used testing
    def search():
        try:
            if request.method == "POST":
                #get request (track name) from the user
                #track_name = request.values['track']
                track_name = "dummy"
            # else:
            #     #set to test track name
            #     track_name = "The Chantels"
        except Exception as e:
            track_name = "Wynona's Big Brown Beaver"
        # track_name = sorted(request.values['track'])
        #     #send track name (possibly find track_id) to ML_function
        # answer = ML_function(track_name)

        #return a jsonified answer
        return render_template('base.html', posts=posts)

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
