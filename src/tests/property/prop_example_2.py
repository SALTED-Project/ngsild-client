import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

# Example to create normal NGSI-LD with nested property in NGSI-LD
'''
    {
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 12,
		'temprature': {
			'type': 'Property',
			'value': {
				'type': 'Fahrenheit',
				'degree': '98.6F'
			}
		}
	}
}
'''
e = Entity("parking", "noidagip")
value = {"type":"Fahrenheit", "degree" : "98.6F"}
e.add_prop("room", 12).add_prop("temprature",value , nested=True)
print(e)