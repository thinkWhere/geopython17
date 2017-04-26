from flask import Blueprint

swagger = Blueprint('swagger', __name__, static_folder='static/swagger-ui-v2', url_prefix='/api-docs')
main = Blueprint('main', __name__, template_folder="templates", static_folder='static/geopython')

from . import controller
