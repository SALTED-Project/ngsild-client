import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client

'''
    The following code snipped show how to get the temporal entity by using EntityId
'''

client_obj = Client("10.10.26.101", "9090")
historical_data = client_obj.get_temporal("urn:ngsi-ld:Vehicle:A135")

print(historical_data)
