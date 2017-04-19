from flask_restful import Resource, request
from micro.services.mapping_service import MappingService


class MappingAPI(Resource):

    def put(self):
        """
        Creates mapping record in db
        ---
        tags:
          - mapping
        produces:
          - application/json
        parameters:
            - in: body
              name: body
              required: true
              description: JSON object for creating draft project
              schema:
                  properties:
                      name:
                          type: string
                          default: test
                      geometry:
                          type: string
                          default: geojson-here
        responses:
            201:
                description: Mapping saved successfully
            500:
                description: Internal Server Error
        """
        mapping_json = request.get_json()
        MappingService.save_feature_collection(mapping_json)
        return {"Feature": "Saved"}, 201

    def get(self, name):
        """
        Simple calculator that multiplies 2 numbers
        ---
        tags:
          - mapping
        produces:
          - application/json
        parameters:
            - name: name
              in: path
              description: Feature Collection to find
              required: true
              type: string
        responses:
            200:
                description: GeoJson Feature Collection
            500:
                description: Internal Server Error
        """
        return MappingService.get_mapping(name)
