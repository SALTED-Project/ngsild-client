from __future__ import annotations
from multipledispatch import dispatch
from ngsildclient.ngsild import LdDict
from ngsildclient.entity import Entity

class UpdateProperty(Entity):
    @dispatch(dict)
    def __init__(self, payload):
        self._current_prop = self._lastprop = self.root = LdDict(payload)
        self.parallel_nested = False
        self._mulstack = []
    
        
        