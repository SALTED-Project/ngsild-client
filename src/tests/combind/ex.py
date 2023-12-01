from geojson.geometry import Point
from ngsildclient.entity import Entity
import sys
sys.path.append("../../../src")

from ngsildclient.entity import Entity

entity_obj = Entity("hgbdf","efbe")
entity_obj.add_prop("a", 123)
print(entity_obj)
