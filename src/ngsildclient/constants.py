from __future__ import annotations
from geojson import (
    Point,
    Polygon,
    LineString,
    MultiLineString,
    MultiPolygon,
    MultiPoint,
)
from dataclasses import dataclass, field
from typing import Union, Any
from datetime import datetime
from enum import Enum

PREFIX = True
CORECONTEXT = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
URN_PREFIX = "urn:ngsi-ld:"
NGSILD_TYPE = "type"
NGSILD_DATASET_ID = "datasetId"
NGSILD_OBSERVED_AT = "observedAt"
NGSILD_UNIT_CODE = "unitCode"
NGSILD_CONTEXT = "@context"
NGSILD_VALUE = "value"
NGSILD_PREVIOUS_VALUE = "previousValue"
NGSILD_UNIT_CODE = "unitCode"
NGSILD_PREVIOUS_OBJECT = "previousObject"
NGSILD_OBJECT = "object"
HTTP_OBJECT = "http://"
NGSILD_IP = "ip"
NGSILD_PORT = "port"
VALUE = "value"

NGSILD_TEMPORAL_ENDPOINT = "/ngsi-ld/v1/temporal/entities"
NGSILD_NORMAL_ENDPOINT = "/ngsi-ld/v1/entities"
NGSILD_TENANT = "tenant"
NGSILD_CONTENT_TYPE = "Content-Type"
NGSILD_NOCONTEXT = "application/json"
NGSILD_CONTEXT = "application/ld+json"
NGSILD_TENANT = "NGSILD_Tenant"
NGSILD_TENANT_PATH = "NGSILD_Path"
NGSILD_BATCH_CREATE = "/ngsi-ld/v1/entityOperations/create"
NGSILD_BATCH_UPSERT = "/ngsi-ld/v1/entityOperations/upsert"
NGSILD_BATCH_QUERY = "/ngsi-ld/v1/entityOperations/query"
NGSILD_BATCH_DELETE = "/ngsi-ld/v1/entityOperations/delete"
NGSILD_BATCH_UPDATE = "/ngsi-ld/v1/entityOperations/update"


@dataclass
class AttrPropValue:
    value: Any
    previous_value: Any = None
    datasetid: str = None
    observedat: Union[str, datetime] = None
    unitcode: str = None


@dataclass
class AttrRelValue:
    object: str
    previous_object: str = None
    datasetid: str = None
    observedat: Union[str, datetime] = None


NGSILD_GEOMETORY = Union[Point, Polygon, LineString,
                         MultiLineString, MultiPolygon, MultiPoint]


@dataclass
class AttrGeoValue:
    value: NGSILD_GEOMETORY
    observedat: Union[str, datetime] = None
    datasetid: str = None


@dataclass
class BatchEntity:
    id: str
    type: str


class AttrType(Enum):
    PROP = "Property"
    TEMPORAL = "Property"
    GEO = "GeoProperty"
    REL = "Relationship"
