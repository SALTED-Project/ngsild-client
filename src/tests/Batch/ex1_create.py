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

def generate_random_number():
    random_number = random.randint(1999, 1000000)
    return random_number
_list = []
for i in range(2):
    e = Entity("School", str(generate_random_number()))
    e.add_prop("room", generate_random_number(), datasetId=str(uuid.uuid1()))
    _list.append(e.to_dict())
client_object = Client("10.10.26.101", 9090)
response = client_object.batch_create(_list)
print(response)

#str(generate_random_number()