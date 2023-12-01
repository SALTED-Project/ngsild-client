import sys
sys.path.append("../../../src")
import ast
import json
from ngsildclient.client import Client
from update_property import UpdateProperty
from ngsildclient.entity import Entity

data = {
	"id": "urn:ngsi-ld:Vehicle:car007",
	"type": "Vehicle",
	"@context": ["https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],
	"brandName": [{
			"type": "Property",
			"value": "Audi",
			"speed": [{
				"type": "Property",
				"value": 50
			}, {
				"type": "Property",
				"value": 70
			}],

			"wheel": {
				"type": "Property",
				"value": 4
			}
		},
		{
			"type": "Property",
			"value": "Mercedes",
			"speed": [{
				"type": "Property",
				"value": 100
			}, {
				"type": "Property",
				"value": 170
			}]
		}
	]
}

test_obj5 = Entity("Vehicle","car009")

print(test_obj5.add_prop("abc",80).nested().add_prop("speed",50, multi=True).add_prop("speed",70))

c= Client("127.0.0.1", "")
c.query(entityids="1234", type = "vehicle")

