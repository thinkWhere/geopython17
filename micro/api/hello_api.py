from flask_restful import Resource


class HelloAPI(Resource):

    def get(self):
        return {"hello": "GeoPython 17"}, 200


class CalcAPI(Resource):

    def get(self, num1: int, num2: int):
        """ Multiplies two numbers together """
        return {"answer": num1 * num2}, 200
