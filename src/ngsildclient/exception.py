from __future__ import annotations


class NgsiError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class NgsiDateError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NgsiUriError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NgsiRelValueError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NgsiGeoValueError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NgsiPropValueEorr(Exception):
    def __inti__(self, msg):
        self.msg = msg


class IPError(Exception):
    def __init__(self, msg):
        self.msg = msg


class PortError(Exception):
    def __init__(self, msg):
        self.msg = msg

class NameError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
class VameError(Exception):
    def __init__(self, msg):
        self.msg = msg