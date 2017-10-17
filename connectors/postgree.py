from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.BaseModel import Base


class PostGreConnector:

    def __init__(self):
        engine = create_engine('postgresql://' + pg_user + ':' + pg_pswd + ' @' + pg_url + '/' + pg_db)
        DBsession = sessionmaker()
        DBsession.bind = engine
        self.session = DBsession()

    def CreateAllTables(self):
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

    def InsertList(self, data):
        self.session.add_all(data)

    def InsertElement(self, element):
        self.session.add(element)