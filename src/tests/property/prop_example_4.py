import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity

from datetime import datetime

# Example to add property with all attribute provided in NGIS_LD sp
'''
{
	"id": "urn:ngsi-ld:vechile:car",
	"type": "vechile",
	"@context": ["https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],
	"tyre": {
		"type": "Property",
		"value": {
			"price": 5000,
             "type": "Property" 
		},
		"rim": {
			"type": "Property",
			"value": {
				"price": 6000
			}
		}
	},
	"brand": {
		"type": "Property",
		"value": "audi"
	}
}
'''

e = Entity("vechile", "car")
type_value = {"price":5000}
rim_value= {"price":6000}
e.add_prop("tyre",type_value).add_prop("rim",rim_value , nested= True)
e.add_prop("brand", "audi")
print(e)