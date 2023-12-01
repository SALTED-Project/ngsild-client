from geojson.geometry import Point
import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


from datetime import datetime

# Add Point coordinates in GeoProperty
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'GeoProperty',
		'value': {
			"coordinates": [12.34, 34.45],
			"type": "Point"
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
value = Point((12.34, 34.45))
entity_obj.add_geoprop("room", value, observedAt=datetime(2023, 4, 12))
print(entity_obj)
