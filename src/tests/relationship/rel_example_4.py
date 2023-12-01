import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add property with all attribute provided in NGIS_LD sp
'''
{
	'id': 'urn:ngsi-ld:vechile:car',
	'type': 'vechile',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'hasRoom': {
		'type': 'Relationship',
		'object': 'house2:smartrooms:room1',
		'hasRoom1': {
			'type': 'Relationship',
			'object': 'house2:smartrooms:room1'
		}
	},
	'hasRoom3': {
		'type': 'Relationship',
		'object': 'house2:smartrooms:room1'
	}
}
'''

entity_obj = Entity("vechile", "car")
entity_obj.add_rel("hasRoom","house2:smartrooms:room1").add_rel("hasRoom1","house2:smartrooms:room1" , nested= True)
entity_obj.add_rel("hasRoom3", "house2:smartrooms:room1")
print(entity_obj)