import dataclasses
from datetime import datetime
from sdv.domaine.entities.abstract_actor_entity import AbstractActorEntity


@dataclasses
class ActorDocument:
    id: int
    first_name: str
    last_name: str
    last_update: datetime


def to_es_document(self, index_name:str=none, es_id:int=1)->dict:
    return {
        "index":index_name,
        "id":es_id,
        "op_type":"index",
        "_source":{
            "id":sefl.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "last_update": self.last_update
        }
    }
