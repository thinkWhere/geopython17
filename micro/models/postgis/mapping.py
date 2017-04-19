from micro import db
from geoalchemy2 import Geometry


class Mapping(db.Model):
    """ Describes an individual mapping feature """
    __tablename__ = "mapping"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    geometry = db.Column(Geometry('GEOMETRYCOLLECTION', srid=4326))  # Equivalent WGS 84
