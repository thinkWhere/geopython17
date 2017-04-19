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
        MappingService.save_mapping_feature(mapping_json)