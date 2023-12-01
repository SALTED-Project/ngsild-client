import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

# create room property as multi_attribute
'''
{
	'id': 'urn:ngsi-ld:test1',
	'type': 'vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': [{
		'type': 'Property',
		'value': 23
	}, {
		'type': 'Property',
		'value': 65
	}]
}
'''

multi_object = Entity("vehicle", "test1")

multi_object.add_prop("room", 23, multi=True).add_prop("room", 65). multi_done()

print(multi_object)