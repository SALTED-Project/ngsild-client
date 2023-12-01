from geojson.geometry import Point
from ngsildclient.entity import Entity
import sys
sys.path.append("../../../src")

# Example to create The following Example
'''
{
	'id': 'urn:ngsi-ld:Vehicle:A135',
	'type': 'Vehicle',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'brandName': {
		'type': 'Property',
		'value': 'Mercedes'
	},
	'speed': [{
		'type': 'Property',
		'value': 55,
		'datasetId': 'urn:ngsi-ld:Property:speedometerA4567-speed',
		'source': {
			'type': 'Property',
			'value': 'Speedometer'
		}
	}, {
		'type': 'Property',
		'value': 11,
		'datasetId': 'urn:ngsi-ld:Property:gpsA4567-speed',
		'source': {
			'type': 'Property',
			'value': 'gps'
		}
	}],
	'speed1': {
		'type': 'Property',
		'value': 12,
		'source': {
			'type': 'Relationship',
			'object': 'Camera:necti'
		}
	}
}
'''
entity_obj = Entity("company", "nec123")
entity_obj.add_prop("indiaBranch", 3).nested()
entity_obj.add_prop("branch1", "Noida", nested=True).add_prop(
    "noOfEmployes", 10000, nested=True)
entity_obj.add_prop("branch2", "Banglore").add_prop(
    "noOfEmployes", 10000, nested=True).describe()
# e.add_loc()
print(entity_obj)
