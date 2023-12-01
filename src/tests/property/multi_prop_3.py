import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


# Example to two multi property

'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': [{
		'type': 'Property',
		'value': 45
	}, {
		'type': 'Property',
		'value': 67
	}],
	'temprature': [{
		'type': 'Property',
		'value': 56
	}, {
		'type': 'Property',
		'value': 56
	}]
}
'''
entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("room", 45, multi=True). add_prop("room", 67).multi_done(
).add_prop("temprature", 56, multi=True).add_prop("temprature", 56).multi_done()
print(entity_obj)
