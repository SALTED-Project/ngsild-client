
import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

'''
{
	'id': 'urn:ngsi-ld:parking:noidagip',
	'type': 'parking',
	'@context': ['https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld'],
	'brandName': [{
		'type': 'Property',
		'value': 'Audi',
		'speed': [{
			'type': 'Property',
			'value': 50
		}, {
			'type': 'Property',
			'value': 70
		}]
	}, {
		'type': 'Property',
		'value': 'Mercedes',
		'speed': [{
			'type': 'Property',
			'value': 100
		}, {
			'type': 'Property',
			'value': 170
		}]
	}]
}
'''

'''c = Client("180.179.214.211", "9090")
print(c.query(type = "TestType"))
'''
e = Entity("parking", "noidagip")
e.add_prop("brandName", "Audi", multi=True).nested().add_prop(

    "speed", 50, multi=True).add_prop("speed", 70).mul_done().describe().add_prop(
    "brandName", "Mercedes").nested().add_prop(
    "speed", 100, multi=True).add_prop("speed", 170).describe().mul_done().mul_done()
print(e)
