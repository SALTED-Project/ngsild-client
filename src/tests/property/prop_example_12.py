import sys
sys.path.append("../../../src")
import ast
import json
from ngsildclient.client import Client
from update_property import UpdateProperty
from ngsildclient.entity import Entity

  
# Create the object for client 
client = Client("10.10.26.101", "9090")


# Get Entity from scorpio Broker for type Test1
entities = client.query(entityids="urn:ngsi-ld:test3")

#print(entities)
# result of get entity
'''
 [{
	'id': 'urn:ngsi-ld:test3',
	'type': 'Test1',
	'a': {
		'type': 'Property',
		'subA': {
			'type': 'Property',
			'value': 123
		},
		'value': 123
	},
	'b': [{
		'type': 'Relationship',
		'object': 'urn:bla'
	}, {
		'type': 'Relationship',
		'object': 'url:bla1'
	}],
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld']
}]
'''

# Get the frist entry 
entity = entities[0]
#print(entity)
myA  = entity.get_attr(['a'])
myA[0]["value"] = 444
myA.append(({'type': 'Property', 'value': 555}))
entity.set_attr(["a"], myA)
#print(entity)

'''
{
	'id': 'urn:ngsi-ld:test3',
	'type': 'Test1',
	'a': [{
		'type': 'Property',
		'subA': {
			'type': 'Property',
			'value': 123
		},
		'value': 444
	}, {
		'type': 'Property',
		'value': 555
	}],
	'b': [{
		'type': 'Relationship',
		'object': 'urn:bla'
	}, {
		'type': 'Relationship',
		'object': 'url:bla1'
	}],
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld']
}
'''
subA = entity.get_attr(['a', 0, 'subA'])
subA[0]["value"] = 3333

entity.set_attr(['a', 0, 'subA'], subA)

#print(entity)

'''
{
	'id': 'urn:ngsi-ld:test3',
	'type': 'Test1',
	'a': [{
		'type': 'Property',
		'subA': [{
			'type': 'Property',
			'value': 3333
		}],
		'value': 444
	}, {
		'type': 'Property',
		'value': 555
	}],
	'b': [{
		'type': 'Relationship',
		'object': 'urn:bla'
	}, {
		'type': 'Relationship',
		'object': 'url:bla1'
	}],
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld']
}
'''


myB = entity.get_attr(['b'])
myB[1]['object'] = 'my:new:urn'
entity.set_attr(['b'], myB)
entity.update_attr(["b",0], "my:other:urn")
print(entity)

'''
{
	'id': 'urn:ngsi-ld:test3',
	'type': 'Test1',
	'a': [{
		'type': 'Property',
		'subA': [{
			'type': 'Property',
			'value': 3333
		}],
		'value': 444
	}, {
		'type': 'Property',
		'value': 555
	}],
	'b': [{
		'type': 'Relationship',
		'object': 'my:other:urn'
	}, {
		'type': 'Relationship',
		'object': 'my:new:urn'
	}],
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld']
}
'''
#upsert_response = client.batch_upsert(entity.to_dict())








