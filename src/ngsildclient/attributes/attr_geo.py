from collections.abc import MutableMapping
from scalpl import Cut
from ngsildclient import constants
from ngsildclient.utils import utils
from geojson.geometry import Point, Polygon, MultiPolygon, MultiLineString, MultiPoint, LineString


class AttrGeoProperty(Cut, MutableMapping):

    def __repr__(self):
        return self.data.__repr__()

    @classmethod
    def build_geo_property(cls, attrGeoProp: constants.AttrGeoValue):
        geo_property = {}
        value = attrGeoProp.value
        if isinstance(value, (Point, Polygon, MultiPolygon, MultiLineString, MultiPoint, LineString)):
            value = value
        else:
            raise Exception("provided type is not supported by NGSLD-Broker")
        geo_property[constants.NGSILD_TYPE] = constants.AttrType.GEO.value
        geo_property[constants.NGSILD_VALUE] = value
        if attrGeoProp.observedat is not None:
            geo_property[constants.NGSILD_OBSERVED_AT] = utils.to_iso8601(
                attrGeoProp.observedat)
        if attrGeoProp.datasetid is not None and isinstance(attrGeoProp.datasetid, str):
            geo_property[constants.NGSILD_DATASET_ID] = utils.prefix(
                attrGeoProp.datasetid)
        return geo_property
