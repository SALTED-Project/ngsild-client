from __future__ import annotations
from multipledispatch import dispatch
from ngsildclient import exception as exp
from ngsildclient.ngsild import LdDict
from ngsildclient.utils import utils
from ngsildclient import constants
from datetime import datetime
import json
import copy
from typing import (
    Sequence,
    Union,
    Any,
    List,
    Tuple,
    Mapping,
)

class Entity:
    @staticmethod
    def build_ngsild_id(id: str) -> str:
        if constants.PREFIX:
            if id.replace(" ", "") == "":
                raise Exception("ID can not be blank")
            return utils.prefix(id)

    @dispatch(dict)
    def __init__(self, payload):
        if not payload.get("id", None):
            raise exp.NgsiError("Entity Id must be required")
        if not payload.get("type", None):
            raise exp.NgsiError("Entity Type Must be required")
        if not payload.get("@context"):
            payload["@context"] = [constants.CORECONTEXT]
        payload["id"] = Entity.build_ngsild_id(payload["id"])
        self._current_prop = self._lastprop = self.root = LdDict(payload)
        self.parallel_nested = False
        self._multi_stack = []
        self.parallel_stack = []
        self.previus_property = {}
        self.multi_status = False

    @dispatch(str, str)
    def __init__(self, type: str, id: str, ctx: list[str] = None):
        id = Entity.build_ngsild_id(id)
        self.__init__(
            {"id": id, "type": type, "@context": ctx or [constants.CORECONTEXT]})

    @dispatch(str, str, list)
    def __init__(self, type: str, id: str, ctx: list = None):
        id = Entity.build_ngsild_id(id)
        self.__init__({"id": id, "type": type, "@context": ctx})

    @dispatch(str, str, dict)
    def __init__(self, type: str, id: str, ctx: dict = None):
        id = Entity.build_ngsild_id(id)
        self.__init__({"id": id, "type": type, "@context": ctx})

    @dispatch(str, str, str)
    def __init__(self, type: str, id: str, ctx: str = None):
        id = Entity.build_ngsild_id(id)
        self.__init__({"id": id, "type": type, "@context": ctx})

    @dispatch(object)
    def __init__(self, id):
        raise Exception(
            "To create an entity id and type is required for example: entity_obj = Entity(id, type)")

    @dispatch(object, object)
    def __init__(self, id, type):
        raise Exception(
            "The supported type for id and type is str and for context it should be list,dict or str")

    @dispatch(object, object, object)
    def __init__(self, id, type, ctx):
        raise Exception(
            "The supported type for id and type is str and for context it should be list,dict or str")

    def nested(self):
        if len(self.parallel_stack) > 0:
            if self.parallel_stack[len(self.parallel_stack)-1] != self.previus_property:
                self.parallel_stack.append(self.previus_property)
        if len(self.parallel_stack) == 0 and len(self.previus_property) != 0:
            self.parallel_stack.append(self.previus_property)
        self.parallel_nested = True
        return self

    def describe(self):
        if len(self.parallel_stack) <= 1:
            self.parallel_nested = False

        if len(self.parallel_stack) > 0:
            self.parallel_stack.pop()
        return self

    def multi_done(self):
        if len(self._multi_stack) <= 1:
            self.multi_status = False
        if len(self._multi_stack) > 0:
            self._multi_stack.pop()
        return self

    def to_dict(self) -> LdDict:
        return self.root.to_dict()

    def _update_multiattribute(self, attr_name: str, property: LdDict, data_dict):
        if attr_name in data_dict and isinstance(data_dict[attr_name], list):
            data_dict[attr_name].append(property)
        else:
            list_ = []
            if attr_name in data_dict:
                list_.append(data_dict[attr_name])
            list_.append(property)
            data_dict[attr_name] = list_

    def _update_entity(self, attr_name: str, property: LdDict, nested: bool = False, multi: bool = False):
        self.previus_property = property
        if nested is True or self.parallel_nested is True:
            if self.parallel_nested == True and nested == True:
                if len(self._multi_stack) > 0 and attr_name in self._multi_stack[len(self._multi_stack) - 1]:
                    self._update_multiattribute(
                        attr_name, property, self._multi_stack[len(self._multi_stack) - 1])
                    self._current_prop = property
                else:
                    self._current_prop[attr_name] = property
                    self._current_prop = property
                if multi == True:
                    self._multi_stack.append(self._current_prop)
            else:
                if len(self._multi_stack) > 0 and attr_name in self._multi_stack[len(self._multi_stack) - 1]:
                    self._update_multiattribute(
                        attr_name, property, self._multi_stack[len(self._multi_stack) - 1])
                    self._current_prop = property
                else:
                    if self.parallel_nested == True:
                        self._lastprop = self.parallel_stack[len(
                            self.parallel_stack) - 1]
                    self._lastprop[attr_name] = property
                    self._current_prop = self._lastprop[attr_name]
                    if multi == True:
                        self._multi_stack.append(self._lastprop)
                    if self.parallel_nested == False and nested == True:
                        self._lastprop = property

        else:
            if len(self._multi_stack) > 0 and attr_name in self._multi_stack[len(self._multi_stack) - 1]:
                self._update_multiattribute(
                    attr_name, property, self._multi_stack[len(self._multi_stack) - 1])
                self._current_prop = self._lastprop = property
            else:
                self._current_prop = self._lastprop = self.root[attr_name] = property
            if multi == True:
                self._multi_stack.append(self.root)

    def __get_attr(self, data, path):
        if len(path) == 0:
            return data
        current_key = path[0]
        if isinstance(data, list):
            if isinstance(current_key, int) and len(data) > current_key:
                return self.__get_attr(data[current_key], path[1:])
            else:
                return []
        if isinstance(data, dict):
            if current_key in data:
                return self.__get_attr(data[current_key], path[1:])
            else:
                return []

    def get_attr(self, path):
        if len(self.root) > 0:
            data = copy.deepcopy(self.root.to_dict())
            result = self.__get_attr(data, path)
            if isinstance(result, list):
                return result
            else:
                return [result]
        else:
            return []

    def __set_attr(self, data, path, new_data):
        current_obj = data
        for key in path[:-1]:
            if isinstance(current_obj, list) and len(current_obj) > key:
                current_obj = current_obj[key]

            elif isinstance(current_obj, dict) and key in current_obj:
                current_obj = current_obj[key]
            else:
                return data
        if isinstance(current_obj, list) and len(current_obj) > path[-1]:
            current_obj[path[-1]] = new_data
        elif path[-1] in current_obj:
            current_obj[path[-1]] = new_data
        return data

    def set_attr(self, path, update_obj) -> Entity:
        self.__set_attr(self.root.to_dict(), path, update_obj)
        return self

    def __update_attr(self, data, path, _object):
        current_obj = data
        for key in path:
            if isinstance(current_obj, dict):
                current_obj = current_obj[key]
            elif isinstance(current_obj, list):
                if isinstance(key, int) and len(current_obj) > key:
                    current_obj = current_obj[key]
                else:
                    raise Exception("key for list can not be string")
            else:
                current_obj = current_obj[key]

        if "value" in current_obj:
            current_obj["value"] = _object

        if "object" in current_obj:
            current_obj["object"] = _object

        return data

    def update_attr(self, path, object) -> Entity:
        self.__update_attr(self.root.to_dict(), path, object)
        return self

    def __ior__(self, prop: Mapping):
        self.root |= prop
        return self

    def add_prop(
            self,
            name: str = None,
            value: Any = None,
            nested: bool = False,
            multi: bool = False,
            previousValue: Any = None,
            observedAt: Union[str, datetime] = None,
            unitCode: str = None,
            datasetId: str = None
    ) -> Entity:
        """
          Description 
          -------------------------------------------------
          This function is responsible to add entity propety into entity

            name : mandatory ---> name of propety 
            value : mandatory ---> value of property it is namdatory as NGSILD spac
            previousValue:    ---> Previous value of same property
            unitCode          ---> Property Value's unit code
            datasetId         ---> It allows identifying a set or group of property values
            nested            ----> it contain two values True and False . True repersent provided name 
                                    is the nested property for previous property
        """

        if name is None or not isinstance(name, str) or name.replace(" ", "") == "":
            raise exp.NameError("Name of property can not be None or Blank")

        if value is None:
            raise exp.VameError("Value of property can not be None")

        property = LdDict.make_property(
            value=value,
            datasetid=datasetId,
            previous_value=previousValue,
            observedat=observedAt,
            unitcode=unitCode
        )
        self._update_entity(name, property, nested, multi)
        return self

    def add_rel(
            self,
            name: str = None,
            object: str = None,
            nested: bool = False,
            multi: bool = False,
            previousObject: str = False,
            observedAt: Union[str, datetime] = None,
            datasetId: str = None
    ) -> Entity:
        """
          Description 
          -------------------------------------------------
          This function is responsible to add entity propety into entity

            name : mandatory ---> name of propety 
            value : mandatory ---> object of relationship it is mandatory as NGSILD spac
            previousValue:    ---> Previous ralationship object Value
            datasetId         ---> It allows identifying a set or group of property values
            nested            ----> it contain two values True and False . True repersent provided name 
                                    is the nested property for previous property
        """
        if name is None or not isinstance(name, str) or name.replace(" ", "") == "":
            raise exp.NameError(
                "Name of Relationship can not be None or Blank")

        if object is None:
            raise exp.VameError("Object of Relationship can be not None")

        relationship = LdDict.make_ralationship(
            object=object,
            datasetid=datasetId,
            previous_object=previousObject,
            observedat=observedAt,
        )
        self._update_entity(name, relationship, nested,
                            multi)  # add Multi here
        return self

    def add_geoprop(
            self,
            name: str = None,
            value: constants.NGSILD_GEOMETORY = None,
            nested: bool = False,
            multi: bool = False,
            observedAt: Union[str, datetime] = None,
            datasetId: str = None
    ) -> Entity:
        """
          Description 
          -------------------------------------------------
          This function is responsible to add entity propety into entity

            name : mandatory ---> name of GeoProperty
            value : mandatory ---> coodinates of GeoLocation
            datasetId         ---> It allows identifying a set or group of property values
            nested            ----> it contain two values True and False . True repersent provided name 
                                    is the nested property for previous property
        """
        if name is None or not isinstance(name, str) or name.replace(" ", "") == "":
            raise exp.NameError("Name of GeoProperty can not be None or Blank")

        if value is None:
            raise exp.VameError("Value of GeoProperty can not be None")

        geo_property = LdDict.make_geoprop(
            value=value,
            observedat=observedAt,
            dataset_id=datasetId,
        )
        self._update_entity(name, geo_property, nested, multi)
        return self

    def add_loc(
            self,
            value=None,
            observedAt: Union[str, datetime] = None,
            datasetId: str = None,
            nested: bool = False,
            multi: bool = True
    ) -> Entity:

        if value is None:
            raise exp.VameError("Value of Location can not be None")

        geo_property = LdDict.make_geoprop(
            value=value,
            observedat=observedAt,
            dataset_id=datasetId,
        )
        self._update_entity("location", geo_property, nested, multi)
        return self

    def __repr__(self):
        return self.root.__repr__()
