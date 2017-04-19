import geojson
import json
from micro.models.postgis.mapping import Mapping


class MappingService:

    @staticmethod
    def save_mapping_feature(mapping_json):

        mapping_geometry = geojson.loads(json.dumps(mapping_json['geometry']))

        if type(mapping_geometry) is not geojson.FeatureCollection:
            raise ValueError('Supplied Geometry is not a FeatureCollection')


