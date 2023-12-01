import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'car': {
		'type': 'Property',
		'value': 'audy',
		'brand': {
			'type': 'Property',
			'value': 'BMW'
		}
	},
	'a': {
		'type': 'Property',
		'value': 12,
		'nestedA': {
			'type': 'Property',
			'value': 98,
			'nestedA_2': {
				'type': 'Property',
				'value': 789
			}
		}
	}
}'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("car", "audy").add_prop("brand", "BMW", nested=True)
entity_obj.add_prop("a", 12). add_prop(
    "nestedA", 98, nested=True).add_prop("nestedA_2", 789, nested=True)

print(entity_obj)
