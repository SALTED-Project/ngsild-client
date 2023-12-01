from __future__ import annotations
from collections.abc import MutableMapping, Mapping
from typing import Union, Any, List, Tuple
from ngsildclient.utils import utils
from scalpl import Cut
from ngsildclient.exception import NgsiError
from ngsildclient import constants
import sys
import os
import json

sys.path.append(os.path.dirname(os.getcwd()))


class AttrRalationObject(Cut, MutableMapping):

    def __repr__(self):
        return self.data.__repr__()

    @classmethod
    def build_relationship(cls, attr_obj: constants.AttrRelValue):
        relationship_ = {}
        object = attr_obj.object
        pre_object = attr_obj.previous_object
        if isinstance(object, str):
            correct_object = utils.prefix(object)
        else:
            raise NgsiError(
                f"Cannot map {type(object)} to NGSI type. {object=}")
        if pre_object != None and isinstance(pre_object, str):
            property[constants.NGSILD_PREVIOUS_VALUE] = pre_object
        relationship_[constants.NGSILD_TYPE] = constants.AttrType.REL.value
        relationship_[constants.NGSILD_OBJECT] = correct_object
        if attr_obj.datasetid is not None and isinstance(attr_obj.datasetid, str):
            relationship_[constants.NGSILD_DATASET_ID] = utils.prefix(
                attr_obj.datasetid)
        if attr_obj.observedat is not None :
            relationship_[constants.NGSILD_OBSERVED_AT] = utils.to_iso8601(
                attr_obj.observedat)
        return relationship_
