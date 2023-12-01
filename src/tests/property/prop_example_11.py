import sys
sys.path.append("../../../src")
import ast
import json
from ngsildclient.client import Client
from update_property import UpdateProperty
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:Vehicle:noida',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'Property',
		'value': 45,
		'temp': {
			'type': 'Property',
			'value': 78
		},
		'temp1': {
			'type': 'Property',
			'value': 98,
			'p1': {
				'type': 'Property',
				'value': 65
			}
		}
	}
}

After Update 
{
	'id': 'urn:ngsi-ld:Vehicle:noida',
	'type': 'Vehicle',
	'room': {
		'type': 'Property',
		'temp': {
			'type': 'Property',
			'value': 78
		},
		'temp1': {
			'type': 'Property',
			'p1': {
				'type': 'Property',
				'value': 191,
				'p2': {
					'type': 'Property',
					'value': 76
				}
			},
			'value': 98
		},
		'value': 45
	}
}

'''


entity_obj = Entity("Vehicle", "noida")

entity_obj.add_prop("room", 45).nested().add_prop(
    "temp", 78).add_prop("temp1", 98).add_prop("p1", 65, nested=True)

client = Client("180.179.214.211", "9090")

res = client.batch_upsert(entity_obj.to_dict())

entity = client.query("urn:ngsi-ld:Vehicle:noida")


attribute = Entity.get_prop(entity, "p1")

print(attribute)

update_obj = UpdateProperty(attribute)

update_obj.add_prop("p2",76)

update_obj.set_prop(191)

print(client.batch_upsert(entity, context = True))
