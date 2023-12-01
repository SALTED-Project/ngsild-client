from __future__ import annotations
from typing import Union
from ngsildclient import constants
from ngsildclient.helper import client_utils as u
from ngsildclient.rest.rest import Rest


class ClientEntity:
    def __init__(self):
        pass

    @classmethod
    def create(
        cls,
        base_url,
        entity,
        entity_id=None,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        if entity_id != None:
            url = base_url+constants.NGSILD_NORMAL_ENDPOINT + "/" + entity_id + "/" + "attrs"
        else:
            url = base_url+constants.NGSILD_NORMAL_ENDPOINT
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.post(entity, url, headers)

    @classmethod
    def partial_update(
        cls,
        base_url,
        entity,
        entity_id,
        attrbute=None,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        if attrbute != None:
            url = base_url+constants.NGSILD_NORMAL_ENDPOINT+"/"+entity_id+"/attrs/"+attrbute
        else:
            url = base_url+constants.NGSILD_NORMAL_ENDPOINT+"/"+entity_id+"/attrs/"
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.patch(entity, url, headers)

    @classmethod
    def delete(
        cls,
        base_url,
        entity_id: str,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_NORMAL_ENDPOINT+"/"+entity_id
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.delete(url, headers)

    @classmethod
    def query(
        cls,
        base_url,
        ids,
        param,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None
    ):
        _path = ""
        if ids != None:
            _path = u.tuple_to_string(ids)
            if _path != "":
                _path = "/" + _path
        if len(param) > 0:
            param_path = u.to_string(param)
            if _path == "":
                _path = "?"+param_path
            else:
                _path = _path + "?"+param_path
        url = base_url+constants.NGSILD_NORMAL_ENDPOINT + _path
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.get(url, headers)
