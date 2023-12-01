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
		'object': 'abc:pqr:123',
		'temp': {
			'type': 'Relationship',
			'object': 'abc:pqr:456'
		},
		'temp1': {
			'type': 'Relationship',
			'object': 'abc:pqr:789'
		},
		'temp3': {
			'type': 'Relationship',
			'object': 'abc:pqr:908'
		},
		'temp4': {
			'type': 'Relationship',
			'object': 'abc:pqr:7654'
		}
	}
}
'''

entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("room", "abc:pqr:123").nested().add_rel("temp", "abc:pqr:456")
entity_obj.add_rel("temp1", "abc:pqr:789")
entity_obj.add_rel("temp3", "abc:pqr:908").add_rel("temp4", "abc:pqr:7654").describe()
print(entity_obj)