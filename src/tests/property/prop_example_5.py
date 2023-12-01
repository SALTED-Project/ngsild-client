import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add property with three lavel of hierarchy 
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 12,
		'temp1': {
			'type': 'Property',
			'value': 23,
			'temp2': {
				'type': 'Property',
				'value': 56,
				'temp3': {
					'type': 'Property',
					'value': 78
				}
			}
		}
	}
}
'''

e = Entity("parking", "noidagip")
e.add_prop("room", 12).add_prop("temp1", 23, nested=True).add_prop("temp2", 56, nested=True)
e.add_prop("temp3", 78, nested=True)
print(e)