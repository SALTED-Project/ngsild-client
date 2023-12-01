from __future__ import annotations

from scalpl import Cut

from typing import Union, Any, List, Tuple

from collections.abc import MutableMapping, Mapping
from datetime import datetime
from ngsildclient.attributes.attr_prop import AttrPropValue
from ngsildclient.attributes.attr_rel import AttrRalationObject
from ngsildclient.attributes.attr_geo import AttrGeoProperty

from ngsildclient import constants


class LdDict(Cut, MutableMapping):

    def __init__(self, data: dict = None, name: str = None):
        super().__init__(data)
        self.name = name

    def __repr__(self):
        return self.data.__repr__()

    def to_dict(self) -> dict:
        return self.data

    @classmethod
    def make_property(
            cls,
            value,
            previous_value: Any = None,
            datasetid: str = None,
            observedat: Union[str, datetime] = None,
            unitcode: str = None,
            attrname: str = None
    ) -> AttrPropValue:
        prop_value = constants.AttrPropValue(
            value, previous_value, datasetid, observedat, unitcode)
        pro_ = AttrPropValue.build_property(prop_value)
        return {attrname: pro_} if attrname else pro_

    @classmethod
    def make_ralationship(
            cls,
            object: str,
            datasetid: str = None,
            previous_object: str = None,
            observedat: Union[str, datetime] = None,
            attrname: str = None
    ) -> AttrRalationObject:
        rel_value = constants.AttrRelValue(
            object, previous_object, datasetid, observedat)
        rel_ = AttrRalationObject.build_relationship(rel_value)
        return {attrname: rel_} if attrname else rel_

    @classmethod
    def make_geoprop(
            cls,
            value: Any = constants.NGSILD_GEOMETORY,
            observedat: Union[str, datetime] = None,
            dataset_id: str = None,
            attrname: str = None
    ) -> AttrGeoProperty:
        geo_value = constants.AttrGeoValue(value, observedat, dataset_id)
        geo_ = AttrGeoProperty.build_geo_property(geo_value)
        return {attrname: geo_} if attrname else geo_
