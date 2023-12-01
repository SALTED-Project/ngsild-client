from ngsildclient import constants
from ngsildclient.utils import utils
import pandas as pd


def add_header(
        context=False,
        ngsild_tenant=None,
        ngsild_path=None
) -> dict:
    headers = {}
    if context == True:
        headers[constants.NGSILD_CONTENT_TYPE] = constants.NGSILD_NOCONTEXT
    else:
        headers[constants.NGSILD_CONTENT_TYPE] = constants.NGSILD_CONTEXT

    if ngsild_tenant != None:
        headers[constants.NGSILD_TENANT] = ngsild_tenant

    if ngsild_path != None:
        headers[constants.NGSILD_TENANT_PATH] = ngsild_path

    return headers


def tuple_to_string(my_tuple):
    if isinstance(my_tuple, str):
        return my_tuple
    id_with_prefix = []
    for entity in my_tuple:
        id_with_prefix.append(entity)
    my_string = ','.join(id_with_prefix)
    return my_string


def to_string(param):
    uri_options = []
    for ele in param.keys():
        if isinstance(param[ele], tuple):
            opt = ele+"=" + tuple_to_string(param[ele])
        else:
            opt = ele+"=" + param[ele]
        uri_options.append(opt)
    my_string = '&'.join(uri_options)
    return my_string
