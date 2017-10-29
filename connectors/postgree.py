from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.BaseModel import Base
from constants import pg_user, pg_pswd, pg_url, pg_db


class PostGreConnector:

    def __init__(self):
        self.engine = create_engine('postgresql://hlopes:lopes_146@pg-cartola.c3pssepl8cax.us-east-2.rds.amazonaws.com:5432/cartoladb')
        DBsession = sessionmaker()
        DBsession.bind = self.engine
        self.session = DBsession()

    def CreateAllTables(self):
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def InsertList(self, data):
        self.session.add_all(data)
        self.session.commit()

    def InsertElement(self, element):
        self.session.add(element)
        self.session.commit()