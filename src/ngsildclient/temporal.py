from __future__ import annotations

from typing import Union


class Temporal:
    def __init__(slef):
        pass

    def add_temporal(
        self,
        *entities
    ) -> Union[list, dict]:
        if len(entities) == 1:
            for entity in entities:
                if isinstance(entity, dict):
                    temp_entity = entity
            return temp_entity
        else:
            temppayload = []
            for entity in entities:
                if isinstance(entity, dict):
                    temppayload.append(entity)
            return temppayload
