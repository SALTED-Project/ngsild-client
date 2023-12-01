import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add relationship with multilavel lavel of hierarchy 
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'hasrel': {
		'type': 'Relationship',
		'object': 'house2:smartrooms:room1',
		'hasrel2': {
			'type': 'Relationship',
			'object': 'house2:smartrooms:room1',
			'hasrel3': {
				'type': 'Property',
				'value': 'house2:smartrooms:room3',
				'hasrel4': {
					'type': 'Relationship',
					'object': 'house2:smartrooms:room5'
				}
			}
		}
	}
}
'''

entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("hasrel", "house2:smartrooms:room1").add_rel("hasrel2", "house2:smartrooms:room1", nested=True).add_prop("hasrel3", "house2:smartrooms:room3", nested=True)
entity_obj.add_rel("hasrel4", "house2:smartrooms:room5", nested=True)
print(entity_obj)