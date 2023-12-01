import json
import pytest
from datetime import datetime
import sys
sys.path.append("../../src")
from ngsildclient.entity import Entity
test_obj = Entity("parking", "huda")

with open("test_data.json") as file:
    data = json.load(file)

# UT0021


def test_add_rel():
    '''
    test to add relation in entity object
    '''
    result = test_obj.add_rel("isPartOf", "HudaComplex")
    assert result.to_dict() == data.get("output_add_rel")

# UT0022


def test_add_rel1():
    '''
    test to add relation in entity object
    '''
    result = test_obj.add_rel(
        "availableSpace", "HudaComplex", observedAt=datetime(2023, 4, 10))
    assert result.to_dict() == data.get("output_add_rel1")

# UT0023


def test_add_rel2():
    '''
    test to add relation in entity object
    '''
    result = test_obj.add_rel("availableSpace", "HudaComplex", observedAt=datetime(
        2023, 4, 11), datasetId="urn:ngsi-ld:availablespace:001")
    assert result.to_dict() == data.get("output_add_rel2")

# UT0024


def test_add_rel3():
    '''
    test to add nested relation in entity object
    '''
    result = test_obj.add_rel(
        "slotavailable", "HudaComplex", observedAt=datetime(2023, 4, 12)).add_prop("slotNo", "245", nested=True)
    assert result.to_dict() == data.get("output_add_rel3")

# UT0025


def test_add_rel4():
    '''
    test to add relation in entity object
    '''
    result = test_obj.add_rel("blockavailable", "HudaComplex", observedAt=datetime(
        2023, 4, 9)).add_rel("floorNo", "urn:ngsi-ld:block", nested=True)
    assert result.to_dict() == data.get("output_add_rel4")

# UT0026


def test_add_rel5():
    '''
    test to add nested relation in entity object
    '''
    result = test_obj.add_rel("isParked", "HudaComplex", observedAt=datetime(2023, 4, 8)).add_rel(
        "providedBy", "urn:ngsi-ld:bob", nested=True).add_rel("blockNo", "986", nested=True)
    assert result.to_dict() == data.get("output_add_rel5")


# UT0027
test_obj1 = Entity("offStreetParking", "Downton2")


def test_add_rel6():
    '''
    test to add relation in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj1.add_rel("providedBy", 123)

# UT0028


def test_add_rel7():
    '''
    test to add relation in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj1.add_rel("providedBy", [123, 789])

# UT0029


def test_add_rel8():
    '''
    test to add relation in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj1.add_rel("providedBy", (123, 789))

# UT0030


def test_add_rel9():
    '''
    test to add relation in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj1.add_rel("providedBy", {"abc": "def"})


# UT0031
test_obj2 = Entity("Vehicle", "car0098")


def test_add_rel10():
    '''
    test to add multi and nested relation in entity object
    '''
    result = test_obj2.add_rel("speed", "urn:ngsi-ld:Camera", multi=True).nested().add_prop("unitCode", "kmh").describe(

    ).add_rel("speed", "urn:ngsi-ld:GPS").nested().add_prop("unitCode", "ms").describe().multi_done()
    assert result.to_dict() == data.get("output_add_rel10")
