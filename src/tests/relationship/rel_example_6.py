import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'myuniqueuri:hasRoom1': {
		'type': 'Relationship',
		'object': 'house2:smartrooms:room1',
		'myuniqueuri:hasRoom2': {
			'type': 'Relationship',
			'object': 'house2:smartrooms:room2'
		},
		'myuniqueuri:hasRoom3': {
			'type': 'Relationship',
			'object': 'house2:smartrooms:room4',
			'myuniqueuri:hasRoom': {
				'type': 'Relationship',
				'object': 'house2:smartrooms:room56'
			}
		}
	}
}
'''

entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("myuniqueuri:hasRoom1","house2:smartrooms:room1" ).nested().add_rel("myuniqueuri:hasRoom2", "house2:smartrooms:room2").describe()
entity_obj.add_rel("myuniqueuri:hasRoom3", "house2:smartrooms:room4", nested=True)
entity_obj.add_rel("myuniqueuri:hasRoom", "house2:smartrooms:room56", nested = True)

print(entity_obj)