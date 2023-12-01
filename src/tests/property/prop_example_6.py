import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
    {
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 12,
		'temp': {
			'type': 'Property',
			'value': 23
		},
		'temp1': {
			'type': 'Property',
			'value': 23,
			'temp3': {
				'type': 'Property',
				'value': 23
			}
		}
	}
'''

e = Entity("parking", "noidagip")
e.add_prop("room", 12).nested().add_prop("temp", 23).describe().add_prop("room1",94, nested=True)
e.add_prop("temp1", 23, nested=True)
e.add_prop("temp3", 23, nested = True)

print(e)