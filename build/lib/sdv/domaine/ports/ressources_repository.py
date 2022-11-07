from typing import List
from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity
from abc import ABCMeta, abstractmethod


class RessourcesRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_all(self) -> List[AbstractActorEntity]:
        raise NotImplementedError

    @abstractmethod
    def find_by_ids(self, ids: List[int]) -> List[AbstractActorEntity]:
        raise NotImplementedError
