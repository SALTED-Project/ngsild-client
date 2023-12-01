import sys
sys.path.append("../../../src")
import ast
import json
from ngsildclient.client import Client
from update_property import UpdateProperty
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
				'value': 23,
				'temp4': {
					'type': 'Property',
					'value': 13
				}
			}
		}
	}
}
'''

entity_obj = Entity("Vehicle", "noida")

entity_obj.add_prop("room", 45).nested().add_prop(
    "temp", 78).add_prop("temp1", 98).add_prop("p1", 65, nested=True)



'''attribute = Entity.get_prop(entity_obj.to_dict(), "p1")
update_obj = UpdateProperty(attribute)
update_obj.add_prop("p2",76)
update_obj.set_prop(191)'''
print(entity_obj)

