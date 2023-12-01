import sys
sys.path.append("../../../src")
from geojson.geometry import MultiLineString
from ngsildclient.entity import Entity
from ngsildclient.client import Client

# Example to create The following Example
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': [{
			'House': 'urn:mytypes:house',
			'hasRoom': 'myuniqueuri:hasRoom'
		},
		'https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'
	],
	'room': [{
		'type': 'Property',
		'value': 12,
		'isPartOf': {
			'type': 'Relationship',
			'object': 'smartbuilding:house2:sensor4711'
		}
	}, {
		'type': 'Property',
		'value': 23
	}, {
		'type': 'Property',
		'value': 45
	}],
	'location': {
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

entity_obj = Entity("parking", "noidagip2")
MultiLineString_ = MultiLineString(
    [[(1.01, 4.003), (2.01, 4.003)], [(3.01, 4.003), (4.01, 4.003)]])
entity_obj.add_prop("room", 12).add_rel(
    "isPartOf", "smartbuilding:house2:sensor4711", nested=True)
entity_obj.add_prop("room", 23)
entity_obj.add_prop("room", 45)

print(entity_obj)
client_obj = Client("180.179.214.211", "9090")
print(client_obj.query("urn:ngsi-ld:parking:noidagip17"))