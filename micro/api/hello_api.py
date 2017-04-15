from flask_restful import Resource


class HelloAPI(Resource):

    def get(self):
        """ Greets the world """
        return {"hello": "GeoPython 17"}, 200
