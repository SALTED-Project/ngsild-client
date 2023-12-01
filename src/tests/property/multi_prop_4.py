import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 45,
		'temprature': [{
			'type': 'Property',
			'value': 96,
			'source': {
				'type': 'Property',
				'value': 89
			}
		}, {
			'type': 'Property',
			'value': 80,
			'source': {
				'type': 'Property',
				'value': 40
			}
		}]
	}
}'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("room", 45).add_prop(
    "temprature", 96, nested=True, multi=True).add_prop("source", 89, nested=True).add_prop("temprature", 80).add_prop("source", 40, nested=True)
print(entity_obj)
