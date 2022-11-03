from sdv.domaine.ports.ressources_repository import RessourcesRepository

class ActorSQLRepository(RessourcesRepository):
    def __init__(self,engine):
        self._engine=engine

    def find_all(self) -> List[AbstractActorEntity]:
        with Session-self._engine as session:
            return (self.._create_entity(actor) for actor in session.query(ActorSQL))
        raise NotImplementedError


    def find_id(self,ids:List[int])-> List[AbstractActorEntity]:
        raise NotImplementedError


    def createEntity



