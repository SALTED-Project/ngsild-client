
from geojson.geometry import Point, Polygon, MultiLineString
from datetime import datetime

import sys
import pytest
import json
sys.path.append("../../src")
from ngsildclient.entity import Entity


with open("test_data.json") as file:
    data = json.load(file)

# UT0044
test_obj1 = Entity("parking", "noidagip")


def test_geo_property1():
    '''
    test to add geo property in entity object
    '''
    value = Point((-8.51, 41.5))
    result = test_obj1.add_geoprop("room", value)
    assert result.to_dict() == data.get("output_geo_prop1")


# UT0045
test_obj2 = Entity("offStreetParking", "Downtown1")


def test_geo_property2():
    '''
    test to add geo property in entity object
    '''
    result = test_obj2.add_geoprop("geometry", Point([45.76, 89.8])).add_prop("name", "Downtown One"
                                                                              ).add_prop("loctaion", Point([23.4, 98.7]), nested=True)
    # print(result)
    assert result.to_dict() == data.get("output_geo_prop2")


# UT0046
test_obj3 = Entity("offStreetParking", "Downtown2")


def test_geo_property3():
    '''
    test to add geo property in entity object
    '''
    result = test_obj3.add_geoprop("geometry", Polygon([(19, 90), (101, 80), (101, 61), (100, 31), (100, 40)]),
                                   observedAt=datetime(2023, 4, 21))
    assert result.to_dict() == data.get("output_geo_prop3")


# UT0047
test_obj4 = Entity("offStreetParking", "Downtown3")


def test_geo_property4():
    '''
    test to add geo property in entity object
    '''
    result = test_obj4.add_geoprop("geometry", Polygon([(19, 90), (101, 80), (101, 61), (100, 31), (100, 40)]),
                                   datasetId="urn:ngsi-ld:geometry:s1")
    assert result.to_dict() == data.get("output_geo_prop4")


# UT0048
test_obj6 = Entity("offStreetParking", "Downtown5")


def test_geo_property5():
    '''
    test to add geo property in entity object
    '''
    result = test_obj6.add_geoprop("geometry", Polygon(
        [(19, 90), (101, 80), (23, 45)])).add_prop("available_sapce", 123, nested=True)
    assert result.to_dict() == data.get("output_geo_prop5")


# UT0049
test_obj7 = Entity("offStreetParking", "Downtown6")


def test_geo_property6():
    '''
    test to add geo property in entity object
    '''
    result = test_obj7.add_geoprop("geometry", Point((19, 90))).add_prop("availableSpace", 121,
                                                                         observedAt=datetime(2023, 4, 21)).add_rel("providedBy", "urn:ngsi-ld:Camera:C1", nested=True)
    assert result.to_dict() == data.get("output_geo_prop6")


# UT0050
test_obj7 = Entity("offStreetParking", "Downtown6")


def test_geo_property7():
    '''
    test to add geo property in entity object
    '''
    with pytest.raises(Exception):
        assert test_obj7.add_geoprop("geometry", ((19, 90)))

# UT0051


def test_geo_property8():
    '''
test to add geo property in entity object
'''
    result = test_obj7.add_geoprop("geometry", Point())
    print(result)
    assert result.to_dict() == data.get("output_geo_prop8")


# UT0052
test_obj8 = Entity("parking", "noidagip1")


def test_geo_property9():
    '''
    test to add geo property in entity object
    '''
    result = test_obj8.add_geoprop("room", MultiLineString(
        [[(23, 45), (24, 65)], [(26.7, 89.5), (12.43, 89.76)]]))
    assert result.to_dict() == data.get("output_geo_prop9")
