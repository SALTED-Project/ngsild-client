
import sys
import pytest
from datetime import datetime
sys.path.append("../../src")
from utils import utils
# UT0059


def test_iso8601():
    '''
    test iso conversion of datetime
    '''
    result = utils.to_iso8601(datetime(2022, 9, 13))
    assert result == "2022-09-13T00:00:00Z"

# UT0060


def test_iso8601_2():
    '''
    test iso conversion of datetime
    '''
    result = utils.to_iso8601(datetime(2021, 10, 23, 8, 30, 55))
    assert result == "2021-10-23T08:30:55Z"

# UT0061


def test_iso8601_3():
    '''
    test iso conversion of datetime
    '''
    with pytest.raises(Exception):
        assert utils.to_iso8601(2021)
# UT0062


def test_iso8601_4():
    '''
    test iso conversion of datetime
    '''
    result = utils.to_iso8601("2023-05-14")
    assert result == "2023-05-14T00:00:00Z"

# UT0063


def test_iso8601_5():
    '''
    test iso conversion of datetime
    '''
    with pytest.raises(Exception):
        assert utils.to_iso8601("1600000000")
