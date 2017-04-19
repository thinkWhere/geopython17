import logging
import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()

# Import all models so that they are registered with SQLAlchemy
from micro.models.postgis import *  # noqa


def create_app():
    """ Bootstrap function to initialise the Flask app and config """
    app = Flask(__name__)

    env = os.getenv('MICRO_ENV', 'Dev')  # default to Dev if config environment var not set
    app.config.from_object(f'micro.config.{env}Config')

    db.init_app(app)

    app.logger.debug('Initialising Blueprints')
    from .web import main as main_blueprint
    from .web import swagger as swagger_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(swagger_blueprint)

    initialise_logger(app)
    app.logger.info('Geopython 17 Microservice starting up :)')

    init_flask_restful_routes(app)

    return app


def initialise_logger(app):
    """ Read environment config then initialise a 2MB rotating log """
    log_dir = app.config['LOG_DIR']
    log_level = app.config['LOG_LEVEL']

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = RotatingFileHandler(log_dir + '/geo17_micro.log', 'a', 2 * 1024 * 1024, 3)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)


def init_flask_restful_routes(app):
    """
    Define the routes the API exposes using Flask-Restful.  See docs here
    http://flask-restful-cn.readthedocs.org/en/0.3.5/quickstart.html#endpoints
    """
    app.logger.info('Initialising API Routes')
    api = Api(app)

    from micro.api.hello_api import HelloAPI, CalcAPI
    from micro.api.swagger_docs_api import SwaggerDocsAPI

    api.add_resource(HelloAPI,       '/api/v1/hello')
    api.add_resource(CalcAPI,        '/api/v1/calc/<int:num1>/multiplied-by/<int:num2>')
    api.add_resource(SwaggerDocsAPI, '/api/docs')
