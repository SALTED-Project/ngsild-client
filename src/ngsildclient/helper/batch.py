from __future__ import annotations
from ngsildclient import constants
from ngsildclient.helper import client_utils as u
from ngsildclient.rest.rest import Rest


class Batch:

    def __init__(self) -> None:
        pass

    @classmethod
    def batch_create(
        cls,
        base_url,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_BATCH_CREATE
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.post(entity, url, headers)

    @classmethod
    def batch_upsert(
        cls,
        base_url,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_BATCH_UPSERT
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        if not isinstance(entity, list):
            entity = [entity]
        return Rest.post(entity, url, headers)

    @classmethod
    def batch_query(
        cls,
        base_url,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_BATCH_QUERY
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.post(entity, url, headers)

    @classmethod
    def batch_update(
        cls,
        base_url,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_BATCH_UPDATE
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        return Rest.post(entity, url, headers)

    @classmethod
    def batch_delete(
        cls,
        base_url,
        entity,
        context=False,
        ngsild_tenant=None,
        ngsild_path=None,
        **options
    ):
        url = base_url+constants.NGSILD_BATCH_DELETE
        headers = u.add_header(context, ngsild_tenant, ngsild_path)
        if isinstance(entity, list) == False:
            raise Exception("Entity ids must be in list")
        return Rest.post(entity, url, headers)
