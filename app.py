""" core of the flask app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Downloads/song_list.sqlite3'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__):

    @app.route("/home")
    def home():
        pass

    @app.route("/about")
    def about():
        return "this is the about page"