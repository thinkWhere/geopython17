from flask_restful import Resource, request
from micro.services.word_generation_service import WordGenerationService


class WordAPI(Resource):

    def put(self, word):
        """
        Creates mapping record in db
        ---
        tags:
          - mapping
        produces:
          - application/json
        parameters:
            - name: word
              in: path
              description: word to draw
              required: true
              type: string
              default: test
        responses:
            201:
                description: Mapping saved successfully
            500:
                description: Internal Server Error
        """
        location = WordGenerationService.generate_letters(word)
        return {"Feature": "Saved", "location": location}, 201
