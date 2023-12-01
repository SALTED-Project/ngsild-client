
import sys
import pytest
import json
sys.path.append("../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client

with open("test_data.json") as file:
    data = json.load(file)


IP ="10.10.26.101"
PORT=9090

#UT0064
def test_connection1():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert Client({"ip":"","port":PORT})
#UT0065
def test_connection2():
    '''
    test to create connection
    '''
    
    with pytest.raises(Exception):
        assert Client({"ip":IP})
#UT0066
def test_connection3():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert Client({"ip":IP,"port":None})
#UT0067
def test_connection4():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert  Client({"ip":None,"port":PORT})
#UT0068
def test_connection5():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert  Client({"port":PORT})
#UT0069
def test_connection6():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert  Client(ip="",port=PORT)

#UT0070
def test_connection7():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert  Client(ip=None,port=PORT)
#UT0071
def test_connection8():
     '''
    test to create connection
    '''
     Client({"ip":IP,"port":PORT})
#UT0072
def test_connection9():
    '''
    test to create connection
    '''
    with pytest.raises(Exception):
        assert Client({"ip":IP,"port":""})
#UT0073
client_obj =   Client({"ip":IP,"port":PORT})
def test_create1():
    '''
    test to create entity
    '''
    entity_obj = Entity("Vehicle", "noida")
    entity_obj.add_prop("room", 45).nested().add_prop(
    "temp", 78).add_prop("temp1", 98).add_prop("p1", 65, nested=True)
    result = client_obj.create(entity_obj.to_dict())
    assert result['status_code'] == 201 or 409
#UT0074
def test_create2():
    '''
    test to create entity
    '''
   
    result = client_obj.create(data.get("output_add_prop"))
    assert result['status_code'] == 201 or 409
#UT0075
def test_create3():
    '''
    test to create entity
    '''
    result = client_obj.create(data.get("output_add_prop1"))
    assert result['status_code'] == 201 or 409
#UT0076
def test_create4():
    '''
    test to create entity
    '''
   
    result = client_obj.create(data.get("output_add_prop2"))
    assert result['status_code'] == 201 or 409
#UT0077
def test_create5():
    '''
    test to create entity
    '''
   
    result = client_obj.create(data.get("output_add_prop6"))
    assert result['status_code'] == 201 or 409
#UT0078
def test_create6():
    '''
    test to create entity
    '''
   
    result = client_obj.create(data.get("output_add_prop7"))
    assert result['status_code'] == 201 or 409
