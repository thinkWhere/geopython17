import geojson
import json
from micro.models.postgis.mapping import Mapping


class MappingService:

    @staticmethod
    def save_feature_collection(mapping_json):
        """ Saves a GEOJson Feature Collection of linestrings to database"""
        mapping_geometry = geojson.loads(json.dumps(mapping_json['geometry']))

        if type(mapping_geometry) is not geojson.FeatureCollection:
            raise ValueError('Supplied Geometry is not a FeatureCollection')

        # Extract all features in the collection, and save in the DB
        for feature in mapping_geometry['features']:
            mapping = Mapping(mapping_json['name'], feature)
            mapping.save()

    @staticmethod
    def get_mapping(name: str):
        """ Get feature collection from db for name """
        return Mapping.get_features_by_name(name)
