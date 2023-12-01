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
	'room': {
		'type': 'Property',
		'value': 12
	}
}
'''
context=[{"House": "urn:mytypes:house", "hasRoom": "myuniqueuri:hasRoom"},"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"]
e = Entity("parking", "noidagip",context)
e.add_prop("room", 12)
print(e)