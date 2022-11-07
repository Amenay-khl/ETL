from typing import Optional, List
import sqlalchemy
from retry import retry
from config import Config
from sdv.domain.documents.document_type import DocumentType
from sdv.domain.extract_resources import ExtractRessoucres

class Manager:

    def __init__(self, config: Config):

        self._config = config
        self._engine = self._build_engine()
        self._extract_resources = ExtractRessoucres(ActorSQLRepository(self._engine))

    @retry(tries=15, delay=5)
    def extract_resources(self, resource_type: str = "actor", ids: Optional[List[int]] = None):
        document_type = DocumentType.from_text(resource_type)
        documents = self._extract_resources.execute(document_type=document_type, ids=ids)
        # now = datetime.now()
        es_documents = []
        for resource in documents:
            es_documents.append(resource.to_es_document(f"{document_type.label}_i", 1))
        return es_documents

    def _build_engine(self):
        database_url = (
            f"mysql+pymysql://"
            f"{self._config.db_username}:"
            f"{self._config.db_password}@"
            f"{self._config.db_host}:"
            f"{self._config.db_port}/"
            f"{self._config.db_name}"
        )
        return sqlalchemy.create_engine(database_url, echo=self._config.echo_sql)

from sdv.infrastructure.sql.repositories.actor_sql_repository import ActorSQLRepository


if __name__ == "__main__":
    conf = Config()
    manager = Manager(conf)
    manager.extract_resources()
    print()
