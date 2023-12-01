from geojson.geometry import MultiPoint
from ngsildclient.entity import Entity
import sys
sys.path.append("../../../src")
# Add Point coordinates in GeoProperty
'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'room': {
		'type': 'GeoProperty',
		'value': {
			"coordinates": [
				[
					[24.40623, 60.17966],
					[24.50623, 60.27966]
				]
			],
			"type": "MultiPoint"
		}
	}
}
'''
entity_obj = Entity("parking", "noidagip")
MultiPoint_ = MultiPoint([[(24.40623, 60.17966), (24.50623, 60.27966)]])
entity_obj.add_geoprop("room", MultiPoint_)
print(entity_obj)
