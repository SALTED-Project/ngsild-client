import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

# Example to create normal NGSI-LD with nested property in NGSI-LD
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'isPartOf': {
		'type': 'Relationship',
		'object': 'smartbuilding:house2:sensor4711',
		'providedBy': {
			'type': 'Relationship',
			'object': 'smartbuilding:house2:sensor432'
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("isPartOf", "smartbuilding:house2:sensor4711").add_rel("providedBy","smartbuilding:house2:sensor432" , nested=True)
print(entity_obj)