from flask_restful import Resource


class HelloAPI(Resource):

    def get(self):
        """
        Greets GeoPython conf
        ---
        tags:
          - hello
        produces:
          - application/json
        responses:
            200:
                description: Says hello
            500:
                description: Internal Server Error
        """
        return {"hello": "GeoPython 17"}, 200


class CalcAPI(Resource):

    def get(self, num1: int, num2: int):
        """
        Simple calculator that multiplies 2 numbers
        ---
        tags:
          - calculator
        produces:
          - application/json
        parameters:
            - name: num1
              in: path
              description: First number to multiply
              required: true
              type: integer
            - name: num2
              in: path
              description: Second number to multiply
              required: true
              type: integer
        responses:
            200:
                description: Answer provided
            500:
                description: Internal Server Error
        """
        return {"answer": num1 * num2}, 200
