from typing import List

from requests import Session

from sdv.domaine.entities.abstract_actor_entity import AbstractActorEntity
from sdv.domaine.entities.actor import Actor
from sdv.domaine.ports.ressources_repository import RessourcesRepository
from sdv.infrastructure.sql.entities.actor_sql import ActorSQL


class ActorSQLRepository(RessourcesRepository):
    def __init__(self, engine):
        self._engine = engine

    def find_all(self) -> List[AbstractActorEntity]:
        with Session - self._engine as session:
            return (self._create_entity(actor) for actor in session.query(ActorSQL))
        raise NotImplementedError

    def find_by_id(self, ids: List[int]) -> List[AbstractActorEntity]:
        raise NotImplementedError

    def create_entity(actor: ActorSQL) -> Actor:
        return Actor(id=actor.id, first_name=actor.first_name, last_name=actor.last_name, last_update=actor.last_update)
