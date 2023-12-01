from geojson.geometry import MultiLineString
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
					[1.01, 4.003],
					[2.01, 4.003]
				],
				[
					[3.01, 4.003],
					[4.01, 4.003]
				]
			],
			"type": "MultiLineString"
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
MultiLineString_ = MultiLineString(
    [[(1.01, 4.003), (2.01, 4.003)], [(3.01, 4.003), (4.01, 4.003)]])
entity_obj.add_geoprop("room", MultiLineString_)
print(entity_obj)
