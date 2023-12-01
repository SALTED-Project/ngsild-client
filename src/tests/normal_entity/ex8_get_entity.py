import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client
import json
import ast

# This example shows how to get normal entity by using Multiple Type

Client_object = Client("10.10.26.101", "9090")
response = Client_object.query(type = ("house, house1"))
print(response)