from dataclasses import dataclass
from datetime import datetime

from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity
from sdv.domain.documents.actor_document import ActorDocument


@dataclass
class Actor(AbstractActorEntity):
    """Class for keeping track of an item in inventory."""

    id: int
    first_name: str
    last_name: str
    last_update: datetime

    def to_document(self) -> ActorDocument:
        return ActorDocument(
            id=self.id, last_name=self.last_name, first_name=self.last_name, last_update=self.last_update
        )
