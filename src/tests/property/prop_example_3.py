import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add property with datetime
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 12,
		'observedAt': '2023-12-03T00:00:00Z'
	}
}
'''
e = Entity("parking", "noidagip")
e.add_prop("room", 12, observedAt = datetime(2023, 12,3))
print(e)