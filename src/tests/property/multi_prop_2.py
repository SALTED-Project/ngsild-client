import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity


# Here in the example Speed is the multiattribute 

'''
{
 "id":"urn:ngsi-ld:Vehicle:A135",
 "type":"Vehicle",
 "brandName":{
   "type":"Property",
   "value":"Mercedes"
 },
 "speed":[{
   "type":"Property",
   "value": 55,
   "datasetId": "urn:ngsi-ld:Property:speedometerA4567-speed",
   "source":{
     "type":"Property",
     "value": "Speedometer"
   }
 },
  {
   "type":"Property",
   "value": 11,
    "datasetId": "urn:ngsi-ld:Property:gpsA4567-speed",
   "source":{
     "type":"Property",
     "value": "GPS"
   }
   },
   {
   "type":"Property",
   "value": 10,
   "source":{
     "type":"Property",
     "value": "CAMERA"
   }
 }]
}'''

entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")

entity_obj.add_prop("brandName","Mercedes").add_prop("speed", 55, multi=True).add_prop("source", "Speedometer", nested=True)
entity_obj.add_prop("speed", 11, datasetId="urn:ngsi-ld:Property:speedometerA4567-speed").add_prop("source", "GPS", nested=True).add_prop("speed", 10, datasetId="urn:ngsi-ld:Property:gpsA4567-speed").add_prop("source", "CAMERA", nested=True)
print(entity_obj)