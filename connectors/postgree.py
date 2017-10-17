from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.orm import sessionmaker


class PostGreConnector:

    def __init__(self):
        engine = create_engine('postgresql://' + pg_user + ':' + pg_pswd + ' @' + pg_url + '/' + pg_db)
        self.Base = declarative_base()
        self.Base.metadata.bind = engine
        DBsession = sessionmaker()
        DBsession.bind = engine
        self.session = DBsession()

    def CreateTable(self, Model):
        self.db.create_table(Model)

    def CreateMultipleTables(self, Models):
        self.db.create_tables(Models)
