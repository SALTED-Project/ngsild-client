import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Relationship',
		'object': 'pqr:abc:123',
		'temp': {
			'type': 'Relationship',
			'object': 'pqr:abc:321'
		},
		'temp1': {
			'type': 'Relationship',
			'object': 'pqr:abc:567',
			'temp3': {
				'type': 'Relationship',
				'object': 'pqr:xyz:3456',
				'temp4': {
					'type': 'Relationship',
					'object': 'pqrst:pqr:2345'
				}
			}
		}
	}
}
'''

entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("room", "pqr:abc:123").nested().add_rel("temp", "pqr:abc:321").describe()
entity_obj.add_rel("temp1", "pqr:abc:567", nested=True)
entity_obj.add_rel("temp3", "pqr:xyz:3456", nested = True).add_rel("temp4", "pqrst:pqr:2345", nested=True)
print(entity_obj)