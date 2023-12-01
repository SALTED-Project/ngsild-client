import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'a': {
		'type': 'Property',
		'value': 12,
		'nestedA': {
			'type': 'Property',
			'value': 98
		}
	}
}'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("a", 12). add_prop("nestedA", 98, nested=True)

print(entity_obj)