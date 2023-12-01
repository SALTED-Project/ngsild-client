

import sys
import pytest
import json
sys.path.append("../../src")
from ngsildclient.entity import Entity
with open("test_data.json") as file:
    data = json.load(file)


entity = Entity(data.get("entity"))
# print(entity)

# UT0053


def test_update1():
    '''
    test  to get the attribute
    '''
    obj = entity.get_attr(["brandName", 1, "speed", 0])
    assert obj == [{"type": "Property", "value": 100}]

# UT0054


def test_update2():
    '''
    test  to update the attribute value
    '''
    result = entity.update_attr(["brandName", 1, "speed", 0], 200)
    assert result.to_dict() == data.get("updated_entity")
# UT0055


def test_update3():
    '''
    test  to get the attribute
    '''
    obj = entity.get_attr(["brandName", 1, "speed", 2])
    assert obj == []

# UT0056


def test_update4():
    '''
    test  to get the attribute
    '''
    obj = entity.get_attr(["brandName", 2, "speed", 2])
    assert obj == []

# UT0057


def test_update5():
    '''
    test  to get the attribute
    '''
    obj = entity.get_attr(["brandName", 0, "wheel"])
    assert obj == [{"type": "Property", "value": 4}]

# UT0058


def test_update6():
    '''
    test  to set the attribute
    '''
    tempA = entity.get_attr(["brandName", 1])
    prop = {"wheel": {"type": "Property", "value": 4}}
    tempA.append(prop)
    entity.set_attr(["brandName", 1], tempA)
    print(entity)
    assert entity.to_dict() == data.get("updated_entity_1")
