from flask import Flask


def create_app():
    """ Bootstrap function to initialise the Flask app and config """
    app = Flask(__name__)

    return app
