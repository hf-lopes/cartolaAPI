from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, DateTime

from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.ext.declarative import api
from datetime import datetime



class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime, default = datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


Base = api.declarative_base(cls=BaseModel)



class Match(Base):

    match_week = Column(Integer, nullable = False)
    home_score = Column(Integer, nullable = False)
    visiting_score = Column(Integer, nullable = False)
    result = Column(String, nullable = False)
    year = Column(Integer, nullable = False, default=2014)


class Position(Base):

    name = Column(String, nullable=False)
    nickname = Column(String, nullable = False)
    year = Column(Integer, nullable=False, default=2014)



class PostgreConnector:
	def __init__(self):
		try:
			engine = create_engine('postgresql://hlopes:lopes_146@pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com:5432/cartoladb')
			DBsession = sessionmaker()
			DBsession.bind = engine
			session = DBsession()
			Base.metadata.create_all(engine)
			Base.metadata.bind = engine
			print('Created')
		except Exception as e:
			print(str(e))

PostgreConnector()
