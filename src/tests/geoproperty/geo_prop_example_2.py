from geojson.geometry import Polygon
from ngsildclient.entity import Entity
import sys
sys.path.append("../../../src")
# Add Point coordinates in GeoProperty
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'GeoProperty',
		'value': {
			"coordinates": [
				[
					[100, 0],
					[101, 0],
					[101, 1],
					[100, 1],
					[100, 0]
				]
			],
			"type": "Polygon"
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
polygon = Polygon([[(100, 0), (101, 0), (101, 1), (100, 1), (100, 0)]])
entity_obj.add_geoprop("room", polygon)
print(entity_obj)
