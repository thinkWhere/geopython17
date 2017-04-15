from flask import current_app, jsonify
from flask_restful import Resource
from flask_swagger import swagger


class SwaggerDocsAPI(Resource):
    """
    This Resource provides a simple endpoint for flask-swagger to generate the API docs,
    https://github.com/gangverk/flask-swagger
    """

    def get(self):
        """ Generates YAML for swagger-ui """
        swag = swagger(current_app)
        swag['info']['title'] = "GeoPython 17 Microservice"
        swag['info']['description'] = "API endpoints for GeoPython 17"
        swag['info']['version'] = "0.0.1"

        return jsonify(swag)
