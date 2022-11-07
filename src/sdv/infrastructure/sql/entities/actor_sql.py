from src.sdv.infrastructure.sql.entities import Base
from sqlalchemy import Column, VARCHAR, Integer, DATETIME


class ActorSQL(Base):
    __tablename__ = 'actor'
    id = Column("actor_id", Integer, primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    last_update = Column(DATETIME)

