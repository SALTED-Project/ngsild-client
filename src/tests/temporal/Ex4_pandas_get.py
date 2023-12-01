import sys
sys.path.append("../../../src")
from ngsildclient.client import Client


'''
  # The following code snipped shows how to get pandas series . 
  # To get pandas seried, the value of pandasSeries should be True
  # Attribute name is required to get the pandas series
'''
client_obj = Client("10.10.26.101", "9090")
pandas_data= client_obj.get_temporal(
    "urn:ngsi-ld:Vehicle:A135", entityType="Vehicle", pandasSeries=True, attribute="speed")

print(pandas_data)
