from __future__ import annotations
from multipledispatch import dispatch

class Batch:
    @dispatch(dict)
    def __init__(self, payload):
        pass
    
    def __init__(self):
        pass

    def add_batch(
            self,
            *entities,
         )->list:
        upsert_payload = []
        for entity in entities :
            if isinstance(entity, dict):
                upsert_payload.append(entity)
        return upsert_payload
    
    def get_batch(
            id: str, 
            type:str
            )-> Batch:
        pass