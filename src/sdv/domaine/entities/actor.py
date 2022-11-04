import dataclasses
from datetime import datetime
from dataclasses import dataclass
from sdv.domaine.documents.actor_document import ActorDocument
from sdv.domaine.entities.abstract_actor_entity import AbstractActorEntity


@dataclass
class Actor(AbstractActorEntity):
    id: int
    first_name: str
    last_name: str
    last_update: datetime

    def to_document(self) -> ActorDocument:
        return ActorDocument(
            id=self.id, first_name=self.first_name, last_name=self.last_name, last_update=self.last_update
        )
