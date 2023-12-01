import sys
sys.path.append("../../../src")
import ast
import json
from ngsildclient.client import Client
from update_property import UpdateProperty
from ngsildclient.entity import Entity

'''
    {
	'id': 'urn:ngsi-ld:test3',
	'type': 'Test1',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'a': {
		'type': 'Property',
		'value': 123,
		'subA': {
			'type': 'Property',
			'value': 123
		}
	},
	'b': [{
		'type': 'Relationship',
		'object': 'urn:bla'
	}, {
		'type': 'Relationship',
		'object': 'url:bla1'
	}]
}
'''
entity_obj = Entity("Test1", "test3")
entity_obj.add_prop("a", 123).add_prop("subA", 123, nested=True).add_rel(
    "b", "urn:bla", multi=True).add_rel("b", "url:bla1").multi_done()
#print(entity_obj)
# Create the object for client 
client = Client("10.10.26.101", "9090")

#Created Entity to the Scorpio Broker
res = client.create(entity_obj.to_dict()) 
print(res)