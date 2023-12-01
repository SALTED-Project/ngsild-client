import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': [{
		'House': 'urn:mytypes:house',
		'hasRoom': 'myuniqueuri:hasRoom'
	}, 'https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'hasroom': {
		'type': 'Relationship',
		'object': 'abc:pqr:123'
	}
}
'''
context=[{"House": "urn:mytypes:house", "hasRoom": "myuniqueuri:hasRoom"},"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"]
entity_obj = Entity("parking", "noidagip",context)
entity_obj.add_rel("hasroom", "abc:pqr:123")
print(entity_obj)