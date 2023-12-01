
import sys
import pytest
import json
sys.path.append("../../src")
from ngsildclient.entity import Entity

with open("test_data.json") as file:
    data = json.load(file)


test_obj = Entity("house", "a1")

# UT001


def test_add_prop():
    '''
    test to add property in entity object
    '''
    result = test_obj.add_prop("room", "r1")
    assert result.to_dict() == data.get("output_add_prop")

# UT002


def test_add_prop_1():
    '''
    test to add property in entity object
    '''
    result = test_obj.add_prop("hall", "h1")
    assert result.to_dict() == data.get("output_add_prop1")

# UT003


def test_add_prop_2():
    '''
    test to add nested property in entity object
    '''
    result = test_obj.add_prop("room2", "r2").add_prop(
        "cupboard", "c1", nested=True)
    assert result.to_dict() == data.get("output_add_prop2")

# UT004


def test_add_prop_3():
    '''
    test to add property multiple nested property in entity object
    '''
    result = test_obj.add_prop("room3", "r3").nested().add_prop("cupboard", "c1").add_prop("drawer", "d1", nested=True).add_prop("door", "d1").add_prop("wood", "w1",
                                                                                                                                                        nested=True).add_prop("particles", "p1", nested=True).add_prop("windows", "w1").describe().add_prop("room4", "r4").add_prop("room5", "r5").add_prop("door", "d1", nested=True)

    assert result.to_dict() == data.get("output_add_prop3")


# UT005
test_obj1 = Entity("Vehicle", "car001")


def test_addprop4():
    '''
    test to add property if value is empty in entity object
    '''
    result = test_obj1.add_prop("speed", "")
    assert result.to_dict() == data.get("output_add_prop4")


# UT006
test_obj2 = Entity("Vehicle", "car002")


def test_addprop5():
    '''
    test to add property if value is None in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj2.add_prop("speed", None)


# UT007
test_obj3 = Entity("Vehicle", "car003")


def test_addprop6():
    '''
    test to add property if speed is empty in entity object
    '''
    result = test_obj2.add_prop("speed", " ")
    assert result.to_dict() == data.get("output_add_prop6")


# UT008
test_obj4 = Entity("Vehicle", "car005")


def test_addprop7():
    '''
    test to add multi property in entity object
    '''
    result = test_obj4.add_prop("speed", 40, multi=True).add_prop("speed", 60)
    assert result.to_dict() == data.get("output_add_prop7")


# UT009
test_obj5 = Entity("Vehicle", "car006")


def test_addprop8():
    '''
    test to add multi property with nested property in entity object
    '''
    result = test_obj5.add_prop("brandName", "Audi").nested().add_prop(
        "speed", 50, multi=True).add_prop("speed", 70).describe()

    assert result.to_dict() == data.get("output_add_prop8")


# UT0010
test_obj6 = Entity("Vehicle", "car007")


def test_addprop9():
    '''
    test to add multi property with nested property in entity object
    '''
    result = test_obj6.add_prop("brandName", "Audi", multi=True).nested().add_prop(
        "speed", 50, multi=True).add_prop("speed", 70).multi_done().describe().add_prop(
        "brandName", "Mercedes").nested().add_prop(
        "speed", 100, multi=True).add_prop("speed", 170).describe().multi_done().multi_done()
    # print(result)
    assert result.to_dict() == data.get("output_add_prop9")


# UT0011
test_obj7 = Entity("Vehicle", "car008")


def test_addprop10():
    '''
    test to add property with None value in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj7.add_prop(
            "brandName", "Mercedes").add_prop("speed", None)


# UT0012
test_obj8 = Entity("testType", "testid")


def test_add_prop11():
    '''
    test to add nested property with various levels of nesting  in entity object
    '''
    result = test_obj8.add_prop("a", 123).nested().add_prop(
        "b", 123).add_prop("subB", 144, nested=True).add_prop("c", 144)
    # print(result)
    assert result.to_dict() == data.get("output_add_prop11")


# UT0013
test_obj9 = Entity({"type": "Vehicle", "id": "2"})


def test_entity_creation1():
    '''
    test creation of entity object
    '''
    result = test_obj9
    assert result.to_dict() == data.get("output_entity1")


# UT0014
test_obj10 = Entity({"type": "Vehicle", "id": "urn:ngsi-ld:Vehicle:car008",
                    "@context": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"})  


def test_entity_creation2():
    '''
    test creation of entity object
    '''
    result = test_obj10
    assert result.to_dict() == data.get("output_entity2")

# UT0015


def test_entity_creation3():
    '''
    test creation of entity object
    '''
    with pytest.raises(Exception):
        assert Entity({"id": "urn:ngsi-ld:Vehicle:car008",
                      "@context": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"})

# UT0016


def test_entity_creation4():
    '''
    test creation of entity object
    '''
    with pytest.raises(Exception):
        assert Entity(
            {"type": "Vehicle", "@context": "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"})

# UT0017


def test_entity_creation5():
    '''
    test creation of entity object
    '''
    with pytest.raises(Exception):
        assert Entity("Vehicle", " ")


# UT0018
test_obj11 = Entity("Vehicle", "car009", [
                    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"])


def test_entity_creation6():
    '''
    test creation of entity object
    '''
    result = test_obj11
    assert result.to_dict() == data.get("output_entity6")


# UT0019
test_obj12 = Entity("Vehicle", "car009", [])


def test_entity_creation7():
    '''
    test creation of entity object
    '''
    result = test_obj12
    assert result.to_dict() == data.get("output_entity7")


# UT0020
test_obj13 = Entity("Vehicle", "car009")


def test_add_prop12():
    '''
    test to add property in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj13.add_prop("speed", (20, 40))
