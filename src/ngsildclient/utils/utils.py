from ngsildclient import constants
from datetime import datetime as dt
from typing import Union


def unprefix(value: str) -> str:
    if value is None:
        return None
    else:
        return value


def is_prefix(value: str) -> bool:
    """
        This function takes a value in string format and check if the value start with urn:ngsi-ld: or not 
        @return: True if value start with urn:ngsi-ld: otherwise False 
    """

    return value.startswith(constants.URN_PREFIX)


def prefix(value: str) -> str:
    """
        This function takes a value in string and append string "urn:ngsi-ld:" if value does not start with urn:ngsi-ld:
        @retrun: return value start with "urn:ngsi-ld:"
    """
    if value is None:
        return None
    return value if is_prefix(value) else f"urn:ngsi-ld:{value}"


def date_to_iso8601(observedat) -> str:
    """
        This function takes date in python datetime format and convert the date into iso8061 format
        @return: retuen date in iso8601 format
    """
    try:
        iso8601 = observedat.isoformat()
        return ngsild_broker_time(iso8601)
    except Exception as err:
        raise Exception(err)


def str_to_iso8601(observedat) -> str:
    """
        This function takes date in string format and convert the date into iso8061 format
        @return: retuen date in iso8601 format
    """
    try:
        iso_string = observedat[:len(observedat)] if observedat[len(
            observedat)-1] == 'z' or 'Z' else observedat
        date_time = dt.fromisoformat(iso_string)
        iso8601 = date_time.isoformat()
        return ngsild_broker_time(iso8601)

    except Exception as err:
        raise Exception(err)


def to_iso8601(observedat) -> str:
    """
        This function is responsible to convert datetime into iso8061 format
        @return: return datetime into iso8601 format
    """
    if isinstance(observedat, dt):
        iso_8601_ = date_to_iso8601(observedat)
        return iso_8601_
    elif isinstance(observedat, str):
        iso_8601_ = str_to_iso8601(observedat)
        return iso_8601_
    else:
        raise Exception("Time format is not correct")


def now_to_iso8061() -> str:
    """
        This functio is responsible to convert current datetime into iso8061 format
        @return: date into iso8061 format
    """
    try:
        now = dt.now()
        iso8601 = now.isoformat()
        return ngsild_broker_time(iso8601)
    except Exception as err:
        raise Exception(err)


def ngsild_broker_time(iso8601: str) -> str:
    """
    @return: datetime into iso8061 format
    """
    return iso8601+'Z'
