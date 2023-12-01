from __future__ import annotations
from ngsildclient.utils import utils
from collections.abc import MutableMapping, Mapping
from typing import Union, Any, List, Tuple
from scalpl import Cut
from ngsildclient.exception import NgsiError
from ngsildclient import constants
import sys
import os
import json

sys.path.append(os.path.dirname(os.getcwd()))


class AttrPropValue(Cut, MutableMapping):

    def __repr__(self):
        return self.data.__repr__()

    @classmethod
    def build_property(cls, attr_value: constants.AttrValue):
        property_ = {}

        value = attr_value.value
        pre_value = attr_value.previous_value
        if isinstance(value, (int, float, str, dict, list)):
            correct_value = value
        else:
            raise NgsiError(f"Cannot map {type(value)} to NGSI type. {value=}")
        property_[constants.NGSILD_TYPE] = constants.AttrType.PROP.value
        property_[constants.NGSILD_VALUE] = correct_value
        if pre_value != None and isinstance(pre_value, (int, float, str, dict, list)):
            property_[constants.NGSILD_PREVIOUS_VALUE] = pre_value

        if attr_value.datasetid is not None and isinstance(attr_value.datasetid, str):
            property_[constants.NGSILD_DATASET_ID] = utils.prefix(
                attr_value.datasetid)
        if attr_value.observedat is not None:
            property_[constants.NGSILD_OBSERVED_AT] = utils.to_iso8601(
                attr_value.observedat)
        if attr_value.unitcode is not None and isinstance(attr_value.unitcode, str):
            property_[constants.NGSILD_UNIT_CODE] = attr_value.unitcode
        return property_
