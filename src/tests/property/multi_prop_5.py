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
		'value': 90,
		'temp1': [{
			'type': 'Property',
			'value': 40
		}, {
			'type': 'Property',
			'value': 897
		}],
		'temp2': [{
			'type': 'Property',
			'value': 40
		}, {
			'type': 'Property',
			'value': 780
		}]
	}
}
'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("room", 90).nested().add_prop(
    "temp1", 40, multi=True).add_prop("temp1", 897).multi_done().add_prop("temp2", 40, multi=True).add_prop("temp2", 780)
print(entity_obj)
