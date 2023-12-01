from geojson.geometry import LineString
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
				[34.8, 87.9],
				[65.9, 87.98],
				[34.7, 86.68]
			],
			"type": "LineString"
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
LineString_ = LineString([
    (34.8, 87.90),
    (65.9, 87.98),
    (34.7, 86.68)
])
entity_obj.add_geoprop("room", LineString_)
print(entity_obj)
