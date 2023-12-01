import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client
import asyncio
import random
import time
import uuid
import datetime
import random



_list = ["urn:ngsi-ld:881552","urn:ngsi-ld:544793" ]
client_object = Client("10.10.26.101", "9090")
response = client_object.batch_delete(_list)
print(response)