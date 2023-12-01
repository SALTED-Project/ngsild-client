import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client
import json
import ast

# The Example shows how to delete entity by using  EntityID

Client_object = Client("10.10.26.101", "9090")
response = Client_object.delete("urn:ngsi-ld:house:id:123")
print(response)

