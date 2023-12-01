import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add property with datetime
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'buildingData': {
		'type': 'Relationship',
		'object': 'smartbuilding:house2:sensor4711',
		'observedAt': '2023-12-03T00:00:00Z'
	}
}
'''
entity_obj = Entity("parking", "noidagip")
entity_obj.add_rel("buildingData", "smartbuilding:house2:sensor4711", observedAt = datetime(2023, 12,3))
print(entity_obj)