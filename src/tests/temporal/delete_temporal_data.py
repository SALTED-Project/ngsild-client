import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client

'''
    The Following code is responsible to delete temporal entity by using entityID
'''

client_obj = Client("10.10.26.101", "9090")
respnse = client_obj.temporal_delete("urn:ngsi-ld:Vehicle:A135")

print(respnse)