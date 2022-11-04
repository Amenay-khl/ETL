from typing import List, Optional

from sdv.domaine.documents.actor_document import ActorDocument
from sdv.domaine.documents.document_type import DocumentType
from sdv.domaine.ports.ressources_repository import RessourcesRepository


class ExtractRessoucres:
    def __init__(self, actor_repository: RessourcesRepository):
        self._ressourcesRepository = {DocumentType.ACTOR: actor_repository}

    def execute(self, document_type: Optional[DocumentType] = None, ids: Optional[List[int]] = None
                ) -> List[ActorDocument]:
        entities = []
        if document_type and document_type in self._ressources_repository:
            entities = (
                self._ressources_repository[document_type].find_all()
                if not ids
                else self._ressources_repository[document_type].find_by_ids(ids)
            )
        elif not document_type:
            entities = [
                entity for repository in self._ressources_repository.values() for entity in repository.find_all()
            ]
        return [entity.to_document() for entity in entities]
