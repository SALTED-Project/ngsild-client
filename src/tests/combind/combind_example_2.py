import sys
sys.path.append("../../../src")
from geojson.geometry import MultiLineString
from ngsildclient.entity import Entity


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
		'value': 12,
		'source': {
			'type': 'Property',
			'value': 'Camera'
		}
	}, {
		'type': 'Property',
		'value': 11,
		'datasetId': 'urn:ngsi-ld:Property:gpsA4567-speed',
		'source': {
			'type': 'Property',
			'value': 'gps'
		}
	}]
}
'''
entity_obj = Entity("Vehicle", "A135")
entity_obj.add_prop("brandName", "Mercedes")
entity_obj.add_prop("speed", 55, datasetId="urn:ngsi-ld:Property:speedometerA4567-speed").add_prop(
    "source",  "Speedometer", nested=True)
entity_obj.add_prop("speed", 12).add_prop("source",  "Camera", nested=True)
entity_obj.add_prop("speed", 11, datasetId="urn:ngsi-ld:Property:gpsA4567-speed").add_prop(
    "source",  "gps", nested=True)

print(entity_obj)
