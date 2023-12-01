import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


# Example to create The following Example
'''
    {
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 12
	}
}
'''


e = Entity("parking", "noidagip")
e.add_prop("room", 12)
print(e)