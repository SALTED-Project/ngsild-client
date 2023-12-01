import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client
import json
import ast


# The Example shows how to publish entity on Scorpio Broker if already entityID is  provided in parameter.

entity_object = Entity("house", "house:id:123")

entity_object.add_prop("room", 60).add_rel(
    "providedBy", "companyX", nested=True).add_prop("temprature", 60)

Client_object = Client("10.10.26.101", "9090")

response = Client_object.create(entity_object.to_dict(), entityID="urn:ngsi-ld:house:id:123")

print(response)