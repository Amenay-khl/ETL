from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


class ActorEsDocument(Document):
    actor_id = Keyword()
    first_name = Text()
    last_name = Text()
    last_update = Date()

    class Index:
        name = 'actoEs'
        settings = {
            "number_of_shards": 2,
        }

    def save(self, **kwargs):
        return super(ActorEsDocument, self).save(**kwargs)
