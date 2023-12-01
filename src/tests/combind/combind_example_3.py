from geojson.geometry import MultiLineString
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
entity_obj = Entity("Vehicle", "A135")
entity_obj.add_prop("brandName", "Mercedes")
entity_obj.add_prop("speed", 55, datasetId="urn:ngsi-ld:Property:speedometerA4567-speed").add_prop(
    "source",  "Speedometer", nested=True)
entity_obj.add_prop("speed1", 12).add_rel("source",  "Camera:necti", nested=True)
entity_obj.add_prop("speed", 11, datasetId="urn:ngsi-ld:Property:gpsA4567-speed").add_prop(
    "source",  "gps", nested=True)

print(entity_obj)
