import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': [{
		'type': 'Property',
		'value': 12
	}, {
		'type': 'Property',
		'value': 12
	}]
}
'''
e = Entity("parking", "noidagip")
e.add_prop("room", 12, multi=True).add_prop("room", 12).mul_done()
print(e)