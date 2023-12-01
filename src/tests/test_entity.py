
from geojson.geometry import Point, Polygon, MultiLineString
import sys
import json
from datetime import datetime
sys.path.append("../../src")
from ngsildclient.entity import Entity

with open("test_data.json") as file:
    data = json.load(file)

testObj = Entity("OffStreetParking", "Downtown1")


# UT0032
def test_add_prop1():
    '''
    test to add property in entity object
    '''
    result = testObj.add_prop("room", 80)
    assert result.to_dict() == data.get("out_ent_add_prop1")

# UT0033


def test_add_prop2():
    '''
    test to add property in entity object
    '''
    result = testObj.add_prop("room1", 90)
    assert result.to_dict() == data.get("out_ent_add_prop2")

# UT0034


def test_add_prop3():
    '''
    test to add property in entity object
    '''
    result = testObj.add_prop("room2", 90).add_prop("room3", 40)
    assert result.to_dict() == data.get("out_ent_add_prop3")

# UT0035


def test_add_prop4():
    '''
    test to add nested property in entity object
    '''
    result = testObj.add_prop("room4", 60).add_prop("room5", 50, nested=True)
    assert result.to_dict() == data.get("out_ent_add_prop4")

# UT0036


def test_add_prop5():
    '''
    test to add nested property in entity object
    '''
    result = testObj.add_prop("room6", 680).add_prop(
        "room7", 500, nested=True).add_prop("room8", 900, nested=True)
    assert result.to_dict() == data.get("out_ent_add_prop5")

# UT0037


def test_add_prop6():
    '''
    test to add property in entity object
    '''
    result = testObj.add_prop("availableRoom", 121,
                              observedAt=datetime(2023, 12, 3))
    assert result.to_dict() == data.get("out_ent_add_prop6")

# UT0038


def test_add_prop7():
    '''
    test to add property in entity object
    '''
    result = testObj.add_prop("room9", 870).add_prop(
        "availableRoom", 121, observedAt=datetime(2023, 12, 3), nested=True)
    assert result.to_dict() == data.get("out_ent_add_prop7")


# UT0039
testObj1 = Entity("Automobile", "car")


def test_add_relation1():
    '''
    test to add relation in entity object
    '''
    result = testObj1.add_rel("hasWheel", "wheel1")
    assert result.to_dict() == data.get("out_ent_add_rel1")

# UT0040


def test_add_relation2():
    '''
    test to add relation in entity object
    '''
    result = testObj1.add_rel("hasBrake", "urn:ngsi-ld:car:brake")
    assert result.to_dict() == data.get("out_ent_add_rel2")


# UT0041
test_obj2 = Entity("Building", "building002", [
    "https://example.com/data-models.context-ngsild.jsonld",
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.3.jsonld"
])


def test_add_prop8():
    '''
    test to add geo property,property in entity object
    '''
    value = {
        "streetAddress": "Grober Stern",
        "addressRegion": "Berlin",
        "addressLocality": "Tiergarten",
        "postalCode": "10557"
    }
    result = test_obj2.add_prop("category", "barn").add_prop("address", value).add_geoprop(
        "location", Point([13.35, 52.5144])).add_prop("name", "Siegessaule Barn")
    assert result.to_dict() == data.get("output_ent_add_prop8")


# UT0042
test_obj3 = Entity("room", "r1")


def test_add_prop9():
    '''
    test to add property in entity object
    '''
    result = test_obj3.add_prop("furniture", 2).nested().add_prop("bed", "sangwan").add_prop(
        "sofa", "seesham", multi=True).add_prop("sofa", "sangwan").multi_done().add_prop("almirah", "a1").nested().add_prop(
        "shelf", "s1").add_prop("box", "b1", nested=True).add_prop("drawer", "d1").describe().describe().add_prop(
        "scenery", "horses")
    assert result.to_dict() == data.get("output_ent_add_prop9")


# UT0043
test_obj4 = Entity("Vehicle", "car009")


def test_add_prop10():
    '''
    test to add property in entity object
    '''
    result = test_obj4.add_prop("brandName", "Audi").add_prop(
        "speed", 50, multi=True).add_prop("speed", 70).multi_done()
    print(result)
    assert result.to_dict() == data.get("output_ent_add_prop10")
