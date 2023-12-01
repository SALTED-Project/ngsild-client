import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'lavel_1': {
		'type': 'Property',
		'value': 12,
		'lavel_2': {
			'type': 'Property',
			'value': 98,
			'lavel_3': {
				'type': 'Property',
				'value': 98,
				'lavel_4': {
					'type': 'Property',
					'value': 98
				}
			}
		}
	}
}'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("lavel_1", 12). add_prop("lavel_2", 98, nested=True).add_prop(
    "lavel_3", 98, nested=True).add_prop("lavel_4", 98, nested=True)

print(entity_obj)
